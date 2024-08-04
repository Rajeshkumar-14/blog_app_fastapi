# Package Import
from fastapi import FastAPI

# Models Import
from . import models

# Database Engine Import
from .database import engine

# Import Router
from .routers import blog, user

# FastAPI Instance
app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

# Database Tables Creation
models.Base.metadata.create_all(engine)