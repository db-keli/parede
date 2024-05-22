from fastapi import APIRouter, Depends, HTTPException, Response, Path, Query, Cookie
from models.user_models import UserSchema, UserRegister
from sqlmodel import Session
from config.database import engine

user_router = APIRouter()

@user_router.post("/register", tags=["creator"])
def register(user: UserRegister):
    
    return {"username": user.username, "password": user.password}

@user_router.post("/login", tags=["creator"])
def login(user: UserSchema):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return {"username": user.username, "password": user.password}