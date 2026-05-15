from app.repositories.category_repository import create_category, get_categories

def create_user_category(db, user_id, name):
    return create_category(db, name, user_id)

def list_user_categories(db, user_id):
    return get_categories(db, user_id)
    