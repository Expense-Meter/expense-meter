from pydantic import BaseModel


class ExpenseBase(BaseModel):
    """
    Shared properties for reading and updating an expense.
    """
    amount: float
    category: str
    description: str

