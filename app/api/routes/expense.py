from fastapi import APIRouter, Depends, Query
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.dependencies.auth import get_current_user
from app.schemas.expense import ExpenseCreate, ExpenseResponse
from app.services.expense_service import create_user_expense, list_user_expense

router = APIRouter()

@router.post("/", response_model= ExpenseResponse)
def create_expense(
    data: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_user_expense(db, current_user.id, data)

@router.get("/", response_model=list[ExpenseResponse])
def get_expenses(
    limit: int = Query(10, le= 100),
    offset: int = 0,
    type: Optional[str]= None,
    start_date: Optional[datetime]=None,
    end_date: Optional[datetime]=None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return list_user_expense(db, current_user.id, limit, offset, type, start_date, end_date)