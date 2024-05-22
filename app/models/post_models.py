from sqlmodel import SQLModel, Field, Relationship
from pydantic import typing, EmailStr

from .user_models import AnonymousUser
import datetime
from typing import Optional


class PostSchema(SQLModel):
    content: Optional[str] = Field(default=None, max_length=500)
    created_at: Optional[datetime.datetime] = Field(default=datetime.datetime.now())
    wall: str = Field(default=None)
    user_id: Optional[int] = Field(default=None, foreign_key="anonymous_user.id")
    
    class Config:
        schema_extra = {
            "example": {
                "content": "hello world",
                "wall": "wall_id",
                "user_id": 1
            }
        }
     
class Post(PostSchema, table=True):
    __tablename__ = "posts"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    wall_creator: AnonymousUser = Relationship(back_populates="posts")

class PostResponse(PostSchema):
    pass