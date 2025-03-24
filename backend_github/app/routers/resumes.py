from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..models import Resume, User
from ..schemas import ResumeCreate, ResumeRead
from ..auth import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ResumeRead, status_code=status.HTTP_201_CREATED)
def create_resume(
        resume_data: ResumeCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user),
):
    """
    Создать новое резюме.
    Привязать к текущему пользователю.
    """
    new_resume = Resume(
        user_id=current_user.id,
        position=resume_data.position,
        skills=resume_data.skills,
        experience=resume_data.experience
    )
    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)
    return new_resume


@router.get("/", response_model=List[ResumeRead])
def list_resumes(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    """
    Получить список всех резюме (доступно только авторизованным).
    Если нужно показывать только свои, используйте фильтр:
    resumes = db.query(Resume).filter(Resume.user_id == current_user.id).all()
    """
    resumes = db.query(Resume).all()
    return resumes


@router.get("/{resume_id}", response_model=ResumeRead)
def get_resume(
        resume_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    """
    Получить одно резюме по ID (только авторизованным).
    Если хотите ограничить просмотр только владельцу - добавьте проверку.
    """
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    # Если хотите, чтобы только владелец мог смотреть:
    # if resume.user_id != current_user.id:
    #     raise HTTPException(status_code=403, detail="Not owner of this resume")

    return resume


@router.put("/{resume_id}", response_model=ResumeRead)
def update_resume(
        resume_id: int,
        resume_data: ResumeCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    """
    Обновить резюме (все поля).
    Только владелец может обновлять.
    """
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    if resume.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not owner of this resume")

    # Обновляем поля
    resume.position = resume_data.position
    resume.skills = resume_data.skills
    resume.experience = resume_data.experience

    db.commit()
    db.refresh(resume)
    return resume


@router.delete("/{resume_id}")
def delete_resume(
        resume_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    """
    Удалить резюме.
    Только владелец.
    """
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    if resume.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not owner of this resume")

    db.delete(resume)
    db.commit()
    return {"message": f"Resume {resume_id} deleted successfully"}
