# Package Import
from fastapi import FastAPI
import uvicorn

# Schemas Import
from .schemas import Blog

# Models Import
from . import models

# Database Engine Import
from .database import engine

# FastAPI Instance
app = FastAPI()

# Database Tables Creation
models.Base.metadata.create_all(engine)


@app.get("/")
def blog():
    return {"message": "Hello World"}


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog is created with {blog.title} and {blog.body}"}


# For Debug
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
