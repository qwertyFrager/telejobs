from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey,
    DateTime, Numeric, func
)
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    hashed_password = Column(String(200), nullable=True)  # Добавили

    # Реальное имя пользователя
    name = Column(String(100), nullable=True)

    # Уникальный email
    email = Column(String(100), unique=True, nullable=False, index=True)

    # Роль: 'worker' или 'employer'
    role = Column(String(20), nullable=False, default="worker")

    # Намерения: 'freelance', 'full_time', 'both'
    intent = Column(String(20), nullable=False, default="freelance")

    # Telegram ID (для связи с аккаунтом в Телеграме)
    telegram_id = Column(String(50), nullable=True)

    # Когда пользователь создан
    created_at = Column(DateTime, server_default=func.now())

    # --- Relationships ---
    # Один пользователь может иметь несколько компаний
    companies = relationship("Company", back_populates="user")

    # Один пользователь может создать несколько jobs (заказов/вакансий)
    jobs = relationship("Job", back_populates="owner")

    # Один пользователь может иметь несколько резюме
    resumes = relationship("Resume", back_populates="user")

    # Избранные вакансии/заказы (Many Favorites)
    favorites = relationship("Favorite", back_populates="user")

    # Отклики на вакансии/заказы
    responses = relationship("Response", back_populates="user")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)

    created_at = Column(DateTime, server_default=func.now())

    # --- Relationship ---
    user = relationship("User", back_populates="companies")


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # 'vacancy' или 'freelance'
    type = Column(String(20), nullable=False)

    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)

    # Для фриланс-заказа - цена, для вакансии - зарплата
    price = Column(Numeric, nullable=True)

    # Статус: 'active', 'archived', 'deleted'
    status = Column(String(20), nullable=False, default="active")

    created_at = Column(DateTime, server_default=func.now())

    # --- Relationships ---
    owner = relationship("User", back_populates="jobs")

    # Избранные (список пользователей, добавивших этот job в избранное)
    favorites = relationship("Favorite", back_populates="job")

    # Отклики
    responses = relationship("Response", back_populates="job")


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    position = Column(String(200), nullable=True)
    skills = Column(Text, nullable=True)
    experience = Column(Text, nullable=True)

    created_at = Column(DateTime, server_default=func.now())

    # --- Relationship ---
    user = relationship("User", back_populates="resumes")


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)

    created_at = Column(DateTime, server_default=func.now())

    # --- Relationships ---
    user = relationship("User", back_populates="favorites")
    job = relationship("Job", back_populates="favorites")


class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    message = Column(Text, nullable=True)

    # 'pending', 'viewed', 'accepted', 'rejected', ...
    status = Column(String(20), nullable=False, default="pending")

    created_at = Column(DateTime, server_default=func.now())

    # --- Relationships ---
    job = relationship("Job", back_populates="responses")
    user = relationship("User", back_populates="responses")
