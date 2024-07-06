import typing
import uuid
from sqlmodel import SQLModel, Field, Relationship
from pydantic import typing, validator

if typing.TYPE_CHECKING:
    from .post_models import Post

from typing import Optional

def generate_username(name: str):
    return name+str(uuid.uuid4()).strip("-")[0]

class UserSchema(SQLModel):
    name: Optional[str] = Field(default=None)
    username: str = Field(default=None)
    password: Optional[str] = Field(default=None)


class AnonymousUser(UserSchema, table=True):
    __tablename__ = "anonymoususer"
    id: Optional[int] = Field(default=None, primary_key=True)

    posts: list["Post"] = Relationship(back_populates="wall_creator")


class UserRegister(SQLModel):
    name: Optional[str] = Field(default=None)
    username: str = Field(default=generate_username)
    password: Optional[str] = Field(default=None)
    password2: Optional[str] = Field(default=None)

    @validator("password2")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        return v


class UserLogin(SQLModel):
    username: str = Field(default=None)
    password: Optional[str] = Field(default=None)
