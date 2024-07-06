import uuid
from models.user_models import AnonymousUser
from sqlmodel import Session, select
from config.database import engine


def select_all_users():   
    with Session(engine) as session:
        statement = select(AnonymousUser)
        users = session.exec(statement=statement).all()
    return users

def add_user_to_db(user: AnonymousUser):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        print(user)
        