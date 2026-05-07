from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserUpdate
from app.services.user_service import create_user, login_user
from app.dependencies.db import get_db

router = APIRouter()

# Create new user
@router.post("/create")
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.email, user.password)
@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    return login_user(db, user.email, user.password)