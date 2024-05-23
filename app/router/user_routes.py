from fastapi import APIRouter, Depends, HTTPException, Response, Path, Query, Cookie
from models.user_models import UserSchema, UserRegister, AnonymousUser
from sqlmodel import Session, select
from config.database import engine
from repository.user_repo import *
from repository.posts_repo import *

user_router = APIRouter()

@user_router.post("/register", tags=["creator"])
async def register(user: UserRegister):
    user = AnonymousUser(name=user.name, username=user.username, password=user.password, id=user.id)
    add_user_to_db(user)
    return {'message': "added"}
    
    
@user_router.post("/login", tags=["creator"])
async def login(user: UserSchema):
    return

@user_router.get("/users", tags=["users"])
async def get_users():
    with Session(engine) as session:
        statement = select(AnonymousUser)
        users = session.exec(statement=statement).all()
    
    return users