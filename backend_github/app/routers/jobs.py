from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..models import Job, User
from ..schemas import JobCreate, JobRead
from ..auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=JobRead, status_code=status.HTTP_201_CREATED)
def create_job(
    job_data: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Создать новую вакансию/заказ (job).
    Требует авторизации. user_id берём из current_user.id.
    """
    new_job = Job(
        user_id=current_user.id,            # Владелец = текущий пользователь
        type=job_data.type,
        title=job_data.title,
        description=job_data.description,
        price=job_data.price,
        status=job_data.status,
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job


@router.get("/", response_model=List[JobRead])
def list_jobs(db: Session = Depends(get_db)):
    """
    Получить список всех вакансий/заказов.
    (Публично доступно, без авторизации, но при желании можно защитить)
    """
    jobs = db.query(Job).all()
    return jobs


@router.get("/{job_id}", response_model=JobRead)
def get_job(job_id: int, db: Session = Depends(get_db)):
    """
    Получить конкретную вакансию/заказ по ID.
    """
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.put("/{job_id}", response_model=JobRead)
def update_job(
    job_id: int,
    job_data: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Обновить вакансию/заказ.
    Требует авторизации.
    Проверим, является ли current_user владельцем.
    """
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Проверяем, тот ли пользователь
    if job.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this job")

    # Обновляем поля
    job.type = job_data.type
    job.title = job_data.title
    job.description = job_data.description
    job.price = job_data.price
    job.status = job_data.status

    db.commit()
    db.refresh(job)
    return job


@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Удалить вакансию/заказ по ID.
    Проверим, что текущий пользователь = владелец
    """
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if job.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this job")

    db.delete(job)
    db.commit()
    return {"message": f"Job {job_id} deleted successfully"}
