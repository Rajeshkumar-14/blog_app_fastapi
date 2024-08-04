from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    email: str
    password: str


class ShowUser(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


class BaseBlog(BaseModel):
    title: str
    description: str
    published: Optional[bool]
    user_id: int


class Blog(BaseBlog):
    class Config:
        from_attributes = True


class ShowBlog(Blog):
    title: str
    description: str
    published: Optional[bool]
    creator: ShowUser

    class Config:
        # 'orm_mode' has been renamed to 'from_attributes' in pydantic 2.x
        from_attributes = True


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
