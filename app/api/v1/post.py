from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.post import PostCreate, PostUpdate
from app.services.post_service import *
from app.dependencies.db import get_db

router = APIRouter()

# Create new Post
@router.post("/")
def create(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post.title, post.content, post.category_id)

# Get all posts
@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return get_post(db)

# Get post by ID
@router.get("/{post_id}")
def get_by_id(post_id: int, db: Session = Depends(get_db)):
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# Update Post
@router.put("/{post_id}")
def update(post_id: int, post_data: PostUpdate, db: Session = Depends(get_db)):
    post = update_post(db, post_id, post_data)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# Delete Post
@router.delete("/{post_id}")
def delete(post_id: int, db: Session = Depends(get_db)):
    post = delete_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted successfully"}