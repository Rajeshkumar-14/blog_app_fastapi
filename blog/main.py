# Package Import
from fastapi import FastAPI, Depends, status, HTTPException
import uvicorn

# Schemas, Models Import
from . import schemas, models

# Database Engine Import
from .database import engine, get_db

# SqlAlchemy
from sqlalchemy.orm import Session

# FastAPI Instance
app = FastAPI()

# Database Tables Creation
models.Base.metadata.create_all(engine)


# Get All Blogs From DB
@app.get("/blogs", status_code=status.HTTP_200_OK)
def all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blogs not found"
        )
    return blogs


# Get a Blog using ID
@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    return blog


# Create a new Blog
@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(**request.model_dump())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


# Delete a Blog
@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"data": f"Blog with id {id} is deleted Successfully."}


# Update a Blog
@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )

    blog.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return {"data": f"Blog with id {id} is updated Successfully."}


# For Debug
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
