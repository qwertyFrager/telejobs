from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..models import Company, User
from ..schemas import CompanyCreate, CompanyRead
from ..auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=CompanyRead, status_code=status.HTTP_201_CREATED)
def create_company(
    company_data: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Создать новую запись о компании.
    Требует авторизации (JWT).
    Дополнительно можно проверить роль (например, только 'employer').
    """
    # Если нужно разрешать создавать компании только работодателям:
    if current_user.role != "employer":
        raise HTTPException(status_code=403, detail="Only employers can create companies")

    new_company = Company(
        user_id=current_user.id,
        name=company_data.name,
        description=company_data.description,
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company


@router.get("/", response_model=List[CompanyRead])
def list_companies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Требуем авторизацию
):
    """
    Получить список всех компаний.
    Доступно ТОЛЬКО авторизованным пользователям.
    """
    companies = db.query(Company).all()
    return companies


@router.get("/{company_id}", response_model=CompanyRead)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Требуем авторизацию
):
    """
    Получить детальную информацию о компании по ID.
    Тоже ТОЛЬКО для авторизованных.
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.put("/{company_id}", response_model=CompanyRead)
def update_company(
    company_id: int,
    company_data: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Обновить существующую компанию.
    Требует авторизации, проверяем владелец ли текущий пользователь.
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    # Проверяем владельца
    if company.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this company")

    # Если нужно проверять роль:
    if current_user.role != "employer":
        raise HTTPException(status_code=403, detail="Only employer can update a company")

    company.name = company_data.name
    company.description = company_data.description

    db.commit()
    db.refresh(company)
    return company


@router.delete("/{company_id}")
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Удалить компанию (полностью или мягко) по ID.
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    if company.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this company")

    db.delete(company)
    db.commit()
    return {"message": f"Company {company_id} deleted successfully"}
