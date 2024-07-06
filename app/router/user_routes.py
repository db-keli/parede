from fastapi import APIRouter, Depends, HTTPException, Response, Path, Query, Cookie
from models.user_models import UserSchema, UserRegister, AnonymousUser, UserLogin
from sqlmodel import Session, select
from config.database import engine
from repository.user_repo import *
from repository.posts_repo import *
from auth.user_auth import AuthHandler

user_router = APIRouter()


@user_router.post("/register", tags=["creator"])
async def register(user: UserRegister):
    users = select_all_users()
    for u in users:
        if u.username == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")
    hashed_pwd = AuthHandler().get_password_hash(user.password)
    username = generate_username(user.name)
    user = AnonymousUser(name=user.name, username=username, password=hashed_pwd)
    add_user_to_db(user)
    return {"message": "added"}


@user_router.post("/login", tags=["creator"])
async def login(user: UserLogin):
    users = select_all_users()
    for u in users:
        if u.username == user.username:
            if AuthHandler().verify_password(user.password, u.password):
                token = AuthHandler().encode_token(user.username)
                return token
    raise HTTPException(status_code=401, detail="Invalid credentials")


@user_router.get("/users", tags=["users"])
async def get_users():
    with Session(engine) as session:
        statement = select(AnonymousUser)
        users = session.exec(statement=statement).all()

    return users
