import typing
from sqlmodel import SQLModel, Field, Relationship
from pydantic import typing, EmailStr, validator

if typing.TYPE_CHECKING:
    from .post_models import Post



import datetime
from typing import Optional

class UserSchema(SQLModel):
    name: Optional[str] = Field(default=None)
    username: str = Field(default=None)
    password: Optional[str] = Field(default=None)
    
    

class AnonymousUser(UserSchema, table=True):
    __tablename__ = "anonymous_user"
    id: Optional[int] = Field(default=None, primary_key=True)
    
    posts: list["Post"] = Relationship(back_populates="wall_creator")
    
    
class UserRegister(UserSchema):
    password2: Optional[str] = Field(default=None)
    
    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v