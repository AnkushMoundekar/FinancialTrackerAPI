from fastapi import APIRouter, Depends

from app.services.category_service import create_user_category, list_user_categories
from app.dependencies.db  import get_db
from app.dependencies.auth import get_current_user
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter()

@router.post("/create", response_model=CategoryResponse)
def create_category(
    data: CategoryCreate,
    db = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_user_category(db, current_user.id, data.name)

@router.get("/", response_model=list[CategoryResponse])
def get_categories(
    db = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return list_user_categories(db, current_user.id)