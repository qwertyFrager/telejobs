from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..models import User
from ..schemas import UserCreate, UserRead


router = APIRouter()


def get_db():
    """
    Простая зависимость, возвращающая сессию БД.
    Сессия будет закрыта после завершения запроса.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserRead)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Создать нового пользователя.
    Принимает данные в формате UserCreate,
    возвращает UserRead (включая id, created_at).
    """
    # Проверка уникальности email
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        role=user_data.role,
        intent=user_data.intent,
        telegram_id=user_data.telegram_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=List[UserRead])
def list_users(db: Session = Depends(get_db)):
    """
    Получить список всех пользователей.
    Возвращает список UserRead.
    """
    users = db.query(User).all()
    return users


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Получить конкретного пользователя по ID.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Полностью обновить пользователя (PUT).
    При желании можно сделать отдельную схему UserUpdate
    для частичного обновления (PATCH).
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Обновляем поля
    user.name = user_data.name
    user.email = user_data.email
    user.role = user_data.role
    user.intent = user_data.intent
    user.telegram_id = user_data.telegram_id

    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Удалить пользователя по ID.
    Возвращает простое сообщение об успехе.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": f"User {user_id} deleted successfully"}
