# Packages
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

# Models and Schemas
from .. import models, schemas

# Password Hashing
from ..hashing import Hash


def get_all(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"No user Available"
        )
    return users


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user


def create(request: schemas.User, db: Session):
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(
        username=request.username, email=request.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
