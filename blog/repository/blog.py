# Packages
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

# Models
from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"No Blog Available."
        )
    return blogs


def get(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(**request.model_dump())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"data": f"Blog with id {id} is deleted Successfully."}


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )

    blog.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return {"data": f"Blog with id {id} is updated Successfully."}
