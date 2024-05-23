import uuid
from models.user_models import AnonymousUser
from sqlmodel import Session
from config.database import engine
def generate_username():
    return str(uuid.uuid4())

def add_user_to_db(user: AnonymousUser):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        print(user)

raise