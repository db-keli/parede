from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.post_routes import post_router
from router.user_routes import user_router

app = FastAPI()

app.include_router(post_router)
app.include_router(user_router)