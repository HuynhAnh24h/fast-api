from sqlalchemy.orm import Session
from app.models.post import Post

# Service layer for Post operations
def create_post(db: Session, title: str, content: str):
    if not title or not content:
        raise ValueError("Title and content are required")
    try:
        post = Post(title=title, content=content)
        db.add(post)
        db.commit()
        db.refresh(post)
        return post
    except Exception:
        db.rollback()
        raise

# Service function to retrieve all posts
def get_post(db: Session):
    return db.query(Post).all()

# Services function to retrieve a post by ID
def get_post_by_id(db:Session, post_id: int):
    if post_id is None:
        return None
    try:        
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            return None
        return post
    except Exception:
        raise 

# Services function to update a post
def update_post(db: Session, post_id: int, data):
    if post_id is None or data is None:
        return None
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            return None
        if data.title:
            post.title = data.title
        if data.content:
            post.content = data.content
        db.commit()
        db.refresh(post)
        return post
    except Exception:
        db.rollback()
        raise

# Services function to delete a post
def delete_post(db:Session, post_id: int):
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            return None 
        db.delete(post)
        db.commit() 
        return post
    except Exception:
        db.rollback()
        raise 