from fastapi import FastAPI
from .schemas import Blog

import uvicorn

app = FastAPI()


@app.get("/")
def blog():
    return {"message": "Hello World"}


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog is created with {blog.title} and {blog.body}"}


# For Debug
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)