from pydantic import BaseModel
from typing import Optional


class ExpenseBase(BaseModel):
    """
    Shared properties for reading and updating an expense.
    """
    amount: float
    category: str
    description: str

class ExpenseCreate(ExpenseBase):
    """
    Properties to receive on expense creation.
    """
    # monthly_limit is optional because we only need it while creating the category - budget for the first time.
    monthly_limit: Optional[float] = None
