# app/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from ..db import SessionLocal
from ..models import User
from ..schemas import UserRegister, UserRead, AuthDetails, Token
from ..auth import (
    verify_password,
    get_password_hash,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=UserRead)
def signup(data: UserRegister, db: Session = Depends(get_db)):
    """
    Регистрация нового пользователя с полями:
    - email, password,
    - name, role, intent, telegram_id
    """
    existing_user = db.query(User).filter_by(email=data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Хэшируем пароль
    hashed_pw = get_password_hash(data.password)

    # Создаём пользователя
    new_user = User(
        email=data.email,
        hashed_password=hashed_pw,
        name=data.name,
        role=data.role,
        intent=data.intent,
        telegram_id=data.telegram_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=Token)
def login(auth_details: AuthDetails, db: Session = Depends(get_db)):
    """
    Логин: проверяет email / password, возвращает JWT-токен
    """
    user = db.query(User).filter_by(email=auth_details.email).first()
    if not user or not verify_password(auth_details.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token)
