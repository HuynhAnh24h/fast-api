from fastapi import FastAPI
from app.dependencies.db import get_db

from app.db.base import Base
from app.db.session import engine

# Import Router from api
from app.api.v1 import post
from app.api.v1 import category
from app.api.v1 import client
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Admin CRUD
app.include_router(post.router, prefix="/api/v1/posts", tags=["posts"])
app.include_router(category.router, prefix="/api/v1/category", tags=["category"])


# Query Client
app.include_router(client.router, prefix="/api/v1/client", tags=["client"])

