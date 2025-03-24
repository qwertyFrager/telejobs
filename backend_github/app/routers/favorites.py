from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..models import Favorite, User, Job
from ..schemas import FavoriteCreate, FavoriteRead
from ..auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=FavoriteRead, status_code=status.HTTP_201_CREATED)
def create_favorite(
    favorite_data: FavoriteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Добавить job в избранное.
    Текущий пользователь -> current_user.id,
    передаём job_id в теле запроса (FavoriteCreate).
    """
    # Убеждаемся, что job с таким id существует
    job = db.query(Job).filter(Job.id == favorite_data.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Проверяем, не добавлена ли уже эта запись
    existing_fav = db.query(Favorite).filter(
        Favorite.user_id == current_user.id,
        Favorite.job_id == favorite_data.job_id
    ).first()

    if existing_fav:
        raise HTTPException(status_code=400, detail="Job is already in favorites")

    new_fav = Favorite(
        user_id=current_user.id,
        job_id=favorite_data.job_id
    )
    db.add(new_fav)
    db.commit()
    db.refresh(new_fav)
    return new_fav


@router.get("/", response_model=List[FavoriteRead])
def list_favorites(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Получить список избранных job для текущего пользователя.
    """
    favorites = db.query(Favorite).filter(
        Favorite.user_id == current_user.id
    ).all()
    return favorites


@router.delete("/{favorite_id}")
def delete_favorite(
    favorite_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Удалить запись из избранного по её ID.
    Проверяем, что запись принадлежит текущему пользователю.
    """
    fav = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if not fav:
        raise HTTPException(status_code=404, detail="Favorite not found")

    if fav.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your favorite item")

    db.delete(fav)
    db.commit()
    return {"message": f"Favorite {favorite_id} removed from your list"}
