from pydantic import BaseModel
from datetime import datetime

class ExpenseCreate(BaseModel):
    amount: float
    type: str
    description: str | None = None
    transaction_date: datetime
    category_id: int | None = None

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    type: str
    description: str | None
    transaction_date: datetime
    category_id: int | None
    class Config:
        from_attributes = True