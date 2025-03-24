# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# ------------------------------------------------------------------------------
# 1. USER SCHEMAS
# ------------------------------------------------------------------------------

class UserBase(BaseModel):
    """
    Общие поля, которые могут использоваться при создании/обновлении пользователя
    """
    name: Optional[str] = None
    email: EmailStr
    role: str = "worker"            # 'worker' или 'employer'
    intent: str = "freelance"       # 'freelance', 'full_time', 'both'
    telegram_id: Optional[str] = None


class UserCreate(UserBase):
    """
    Поля, необходимые при создании пользователя
    (Если нужна регистрация по паролю — добавьте поле password)
    """
    pass


class UserRead(UserBase):
    """
    То, что будем возвращать клиенту при получении данных о пользователе
    """
    id: int
    created_at: datetime

    # Позволяет Pydantic брать данные напрямую из ORM-модели
    class Config:
        orm_mode = True


# ------------------------------------------------------------------------------
# 2. COMPANY SCHEMAS
# ------------------------------------------------------------------------------

class CompanyBase(BaseModel):
    name: str
    description: Optional[str] = None


class CompanyCreate(CompanyBase):
    """
    При создании компании можно указать поля из CompanyBase.
    user_id обычно берем из контекста (кто сейчас авторизован),
    но при желании можно добавить сюда, если создаёте для чужого пользователя.
    """
    pass


class CompanyRead(CompanyBase):
    """
    То, что возвращаем при чтении компании
    """
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ------------------------------------------------------------------------------
# 3. JOB SCHEMAS
# ------------------------------------------------------------------------------

class JobBase(BaseModel):
    type: str                      # 'vacancy' или 'freelance'
    title: str
    description: Optional[str] = None
    price: Optional[float] = None  # зарплата или бюджет/оплата за фриланс
    status: str = "active"         # 'active', 'archived', 'deleted'


class JobCreate(JobBase):
    """
    При создании указываем поля. user_id определяют из текущей сессии/токена.
    """
    pass


class JobRead(JobBase):
    """
    Чтение данных о вакансиях/заказах
    """
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ------------------------------------------------------------------------------
# 4. RESUME SCHEMAS
# ------------------------------------------------------------------------------

class ResumeBase(BaseModel):
    position: Optional[str] = None
    skills: Optional[str] = None
    experience: Optional[str] = None


class ResumeCreate(ResumeBase):
    """
    При создании резюме
    """
    pass


class ResumeRead(ResumeBase):
    """
    При чтении резюме
    """
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ------------------------------------------------------------------------------
# 5. FAVORITE SCHEMAS
# ------------------------------------------------------------------------------

class FavoriteBase(BaseModel):
    """
    Связь "пользователь добавил job в избранное"
    """
    pass


class FavoriteCreate(FavoriteBase):
    job_id: int


class FavoriteRead(FavoriteBase):
    id: int
    user_id: int
    job_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ------------------------------------------------------------------------------
# 6. RESPONSE SCHEMAS
# ------------------------------------------------------------------------------

class ResponseBase(BaseModel):
    """
    Отклик на вакансию/заказ
    """
    message: Optional[str] = None
    status: str = "pending"   # 'pending', 'viewed', 'accepted', 'rejected', etc.


class ResponseCreate(ResponseBase):
    pass


class ResponseRead(ResponseBase):
    id: int
    job_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True



# Схемы для авторизации

class AuthDetails(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserRegister(BaseModel):
    """
    Схема для регистрации нового пользователя.
    Помимо email/password,
    включает имя, роль, intent и telegram_id.
    """
    email: EmailStr
    password: str
    name: Optional[str] = None
    role: str = "worker"       # 'worker' / 'employer'
    intent: str = "freelance"  # 'freelance' / 'full_time' / 'both'
    telegram_id: Optional[str] = None