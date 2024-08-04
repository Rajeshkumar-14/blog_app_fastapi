# Package
from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session

# DataBase
from ..database import get_db

# Schema
from .. import schemas

# Repository
from ..repository import user


router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def all_users(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_users(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)
