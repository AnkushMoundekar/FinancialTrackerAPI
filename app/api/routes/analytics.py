from fastapi import APIRouter, Depends

from app.dependencies.db import get_db
from app.dependencies.auth import get_current_user
from app.services.expense_service import get_expense_summary, get_category_summary_service

router = APIRouter()

@router.get("/summary")
def get_summary_api(
    db = Depends(get_db),
    user = Depends(get_current_user)
):
    return get_expense_summary(db, user.id)

@router.get("/by-category")
def get_category_summary_api(
    db = Depends(get_db),
    user = Depends(get_current_user)
):
    return get_category_summary_service(db, user.id)