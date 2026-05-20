from sqlalchemy.orm import Session

from app.models.category import Category


def create_category(db: Session, name: str, user_id: int| None):
    category = Category(name = name, user_id = user_id)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category

def get_categories(db: Session, user_id: int):
    return db.query(Category).filter(
        Category.is_deleted == False, 
        (Category.user_id == None) | (Category.user_id == user_id)).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(
        Category.is_deleted == False,
        Category.id == category_id
    ).first()