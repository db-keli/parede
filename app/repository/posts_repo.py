from models.post_models import Post
from config.database import session
from sqlmodel import Session, select, or_

def select_wall_posts(wall, wall_creator):
    with session:
        statement = select(Post).where(Post.wall == wall and Post.wall_creator == wall_creator)
        posts = session.exec(statement).all()
        return posts