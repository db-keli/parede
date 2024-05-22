from fastapi import APIRouter, Depends, HTTPException, Response, Path, Query, Cookie
from models.post_models import PostSchema, PostResponse
from repository.posts_repo import select_wall_posts

post_router = APIRouter()

@post_router.get("/{username}/{wall_id}/posts", tags=["posts"], response_model=PostResponse)
async def get_posts(username: str, wall_name: str):
    posts = select_wall_posts(wall_name, username)
    return posts

@post_router.post("/{username}/{wall_name}/posts", tags=["posts"])
def create_post(username: str, wall_name: str, post: PostSchema):
    print(username, wall_name, post) 
    return {"content": post.content, "created_at": post.created_at}