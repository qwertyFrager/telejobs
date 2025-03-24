from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..models import Response, User, Job
from ..schemas import ResponseCreate, ResponseRead
from ..auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ResponseRead, status_code=status.HTTP_201_CREATED)
def create_response(
    response_data: ResponseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Создать новый отклик.
    Проверяем, что job существует и не принадлежит этому же пользователю (если нужно).
    """
    job = db.query(Job).filter(Job.id == response_data.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Если хотите запретить откликаться на свою же вакансию:
    if job.user_id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot respond to your own job")

    # Проверяем, нет ли уже отклика (если нужно запрещать дубли)
    existing = db.query(Response).filter(
        Response.job_id == response_data.job_id,
        Response.user_id == current_user.id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="You have already responded")

    new_resp = Response(
        job_id=response_data.job_id,
        user_id=current_user.id,
        message=response_data.message,
        status="pending"  # По умолчанию
    )
    db.add(new_resp)
    db.commit()
    db.refresh(new_resp)
    return new_resp


@router.get("/", response_model=List[ResponseRead])
def list_responses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Возвращает список откликов, зависящий от роли пользователя:
    - worker -> отклики, где user_id = current_user.id
    - employer -> отклики на jobs, где job.user_id = current_user.id
    Можно адаптировать логику по нуждам.
    """
    if current_user.role == "worker":
        responses = db.query(Response).filter(Response.user_id == current_user.id).all()
    elif current_user.role == "employer":
        # Все отклики к вакансиям, которые принадлежат этому работодателю
        # Нужно соединить таблицы Response и Job
        # вариант через JOIN:
        responses = (db.query(Response)
                        .join(Job, Job.id == Response.job_id)
                        .filter(Job.user_id == current_user.id)
                        .all())
    else:
        # Если у вас есть ещё роли, обрабатывайте отдельно
        responses = []
    return responses


@router.get("/{response_id}", response_model=ResponseRead)
def get_response(
    response_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Получить конкретный отклик, если user - владелец отклика
    или если user - владелец job.
    """
    resp = db.query(Response).filter(Response.id == response_id).first()
    if not resp:
        raise HTTPException(status_code=404, detail="Response not found")

    job = db.query(Job).filter(Job.id == resp.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Проверяем, что либо worker == resp.user_id, либо employer == job.user_id
    if not (resp.user_id == current_user.id or job.user_id == current_user.id):
        raise HTTPException(status_code=403, detail="Access denied")

    return resp


@router.put("/{response_id}", response_model=ResponseRead)
def update_response(
    response_id: int,
    response_data: ResponseCreate,  # в простом случае, переиспользуем ResponseCreate
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Обновить отклик.
    Варианты логики:
    - если worker (resp.user_id == current_user.id), меняем message
    - если employer (job.user_id == current_user.id), меняем status
    """
    resp = db.query(Response).filter(Response.id == response_id).first()
    if not resp:
        raise HTTPException(status_code=404, detail="Response not found")

    job = db.query(Job).filter(Job.id == resp.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if current_user.role == "worker":
        # Должен быть владельцем отклика
        if resp.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not your response")
        # Обновим только message (пример)
        resp.message = response_data.message or resp.message
        # status не меняем
    elif current_user.role == "employer":
        # Должен быть владельцем job
        if job.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not your job")
        # Меняем статус (например, pending -> accepted/rejected)
        # Можно хранить в response_data.status (если schema позволяет)
        # Или так:
        # resp.status = response_data.status or resp.status
        # Пока для примера просто сделаем resp.status = "accepted"
        resp.status = "accepted"
    else:
        raise HTTPException(status_code=403, detail="Invalid role")

    db.commit()
    db.refresh(resp)
    return resp


@router.delete("/{response_id}")
def delete_response(
    response_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Удалить отклик.
    Разрешим это владельцу отклика (worker) или владельцу job (employer).
    """
    resp = db.query(Response).filter(Response.id == response_id).first()
    if not resp:
        raise HTTPException(status_code=404, detail="Response not found")

    job = db.query(Job).filter(Job.id == resp.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Проверяем право на удаление
    if resp.user_id != current_user.id and job.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")

    db.delete(resp)
    db.commit()
    return {"message": f"Response {response_id} deleted"}
