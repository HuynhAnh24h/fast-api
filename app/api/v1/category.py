from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.category import CategoryCreate, CategoryUpdate
from app.services.category_service import *
from app.dependencies.db import get_db

router = APIRouter()

# Create new post
@router.post("/")
def create(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category.name)

# Get all category
@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return get_categories(db)

# Get category by id
@router.get("/{category_id}")
def get_by_id(category_id: int, db: Session = Depends(get_db)):
    category = get_by_id(db,category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return Category

# Update category
@router.put("/{category_id}")
def update(category_id: int, category_data: CategoryUpdate, db: Session = Depends(get_db)):
    category = update_category(db, category_id , category_data)
    if category is None:
        raise HTTPException(status_code=404, detail="Category Not Found")
    return category

# delete Category
@router.delete("/{category_id}")
def delete(category_id: int, db: Session = Depends(get_db)):
    category = delete_category(db, category_id)
    if category is None: 
        raise HTTPException(status_code=404, detail="Category not found")
    return {"detail":"category delete success", "data": category}