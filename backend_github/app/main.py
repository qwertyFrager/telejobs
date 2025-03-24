# app/main.py

from fastapi import FastAPI
from .db import Base, engine
from . import models  # важно: чтобы модели были загружены
from .routers import auth, users, jobs, companies, resumes, favorites, responses  # <-- импортируем модуль с роутами

app = FastAPI(title="TeleJobs Backend")


@app.on_event("startup")
def startup_event():
    # Создаёт таблицы, если они не существуют
    Base.metadata.create_all(bind=engine)


# Подключаем роуты
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(companies.router, prefix="/companies", tags=["Companies"])
app.include_router(resumes.router, prefix="/resumes", tags=["Resumes"])
app.include_router(favorites.router, prefix="/favorites", tags=["Favorites"])
app.include_router(responses.router, prefix="/responses", tags=["Responses"])





@app.get("/")
def root():
    return {"message": "Hello from FastAPI + PostgreSQL"}
