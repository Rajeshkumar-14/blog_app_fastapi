# Package
from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session

# DataBase
from ..database import get_db

# Schema
from .. import schemas

# Repository
from ..repository import blog

# Authentication
from ..OAuth2 import get_current_user

# Router Instance
router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
    dependencies=[Depends(get_current_user)],
)


# Get All Blogs
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all_blog(
    db: Session = Depends(get_db),
):
    return blog.get_all(db)


# Get a Blog using ID
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    return blog.get(id, db)


# Create a new Blog
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


# Delete a Blog
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)


# Update a Blog
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)
