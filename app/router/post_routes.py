from fastapi import APIRouter, Depends, HTTPException, Response, Path, Query, Cookie
from models.post_models import PostSchema, PostResponse, Post
from repository.posts_repo import select_wall_posts, add_post_to_db

post_router = APIRouter()


@post_router.get("/{username}/{wall_name}/posts", tags=["posts"])
async def get_posts(username: str, wall_name: str):
    posts = select_wall_posts(wall_name, username)
    return posts


@post_router.post("/{username}/{wall_name}/posts", tags=["posts"])
async def create_post(username: str, wall_name: str, post: PostSchema):
    add_post_to_db(post, username, wall_name)
    return {"message": "post created"}
