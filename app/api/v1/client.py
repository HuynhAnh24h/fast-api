from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.services.client_service import get_post_by_category

router = APIRouter()

@router.get("/category/{category_id}")
def get_posts(category_id: int, db: Session = Depends(get_db)):
    return get_post_by_category(db, category_id)