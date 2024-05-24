from models.post_models import Post, PostSchema
from config.database import session
from sqlmodel import Session, select, or_
from config.database import engine
from models.user_models import AnonymousUser
from datetime import datetime


def select_wall_posts(wall, wall_creator):
    with Session(engine) as session:
        statement = (
            select(Post)
            .join(AnonymousUser, Post.user_id == AnonymousUser.id)
            .where(AnonymousUser.username == wall_creator, Post.wall == wall)
        )
        results = session.exec(statement)
        posts = results.all()
        if not posts:
            return {"message": "No posts found"}
        return posts


def add_post_to_db(post: PostSchema, username, wall_name):
    with Session(engine) as session:
        user = session.exec(
            select(AnonymousUser).where(AnonymousUser.username == username)
        ).first()
        postdb = Post.model_validate(post)
        postdb.wall_creator = user
        postdb.wall = wall_name
        session.add(postdb)
        session.commit()
        session.refresh(postdb)
