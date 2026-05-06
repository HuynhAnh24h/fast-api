from sqlalchemy.orm import Session
from app.models.category import Category
from app.utils.helper import generate_slug


# helper
def _get_category_or_none(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


# create
def create_category(db: Session, name: str):
    try:
        slug = generate_slug(name)
        category = Category(name=name, slug=slug)

        db.add(category)
        db.commit()
        db.refresh(category)

        return category

    except Exception:
        db.rollback()
        raise


# get all
def get_categories(db: Session):
    return db.query(Category).all()


# get by id
def get_category_by_id(db: Session, category_id: int):
    if category_id is None:
        return None

    return _get_category_or_none(db, category_id)


# update
def update_category(db: Session, category_id: int, data):
    if category_id is None:
        return None

    try:
        category = _get_category_or_none(db, category_id)
        if category is None:
            return None

        if data.name is not None:
            category.name = data.name
            category.slug = generate_slug(data.name)

        db.commit()
        db.refresh(category)

        return category

    except Exception:
        db.rollback()
        raise


# delete
def delete_category(db: Session, category_id: int):
    if category_id is None:
        return None

    try:
        category = _get_category_or_none(db, category_id)
        if category is None:
            return None

        db.delete(category)
        db.commit()

        return category

    except Exception:
        db.rollback()
        raise