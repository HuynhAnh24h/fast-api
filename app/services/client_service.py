from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.category import Category
from app.models.post import Post

def get_post_by_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category.posts


# def get_posts_by_category(db: Session, category_id: int):
#     return (
#         db.query(Post)
#         .join(Category)
#         .filter(Category.id == category_id)
#         .all()
#     )