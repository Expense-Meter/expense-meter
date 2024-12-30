from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List
from XpenseMeter import schemas, crud
from XpenseMeter.db.session import get_db
from XpenseMeter.decorators.jwt import token_authentication_required
from XpenseMeter.utils import email

router = APIRouter()

@router.get("/", response_model=List[schemas.ExpenseBase])
@token_authentication_required
async def read_expenses(request: Request, db: Session = Depends(get_db)):
    """
    Retrieve all expenses.
    """
    return crud.get_current_month_expenses(db, user_id=request.state.user_id)

@router.post("/", response_model=schemas.ExpenseBase)
@token_authentication_required
async def add_expense(request: Request, expense_in: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    """
    Add a new expense.
    """
    category = crud.get_category(db, category_name=expense_in.category, user_id=request.state.user_id)
    if not category:
        if expense_in.monthly_limit is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Monthly limit is required for a new category",
            )
        crud.add_category(db, category_name=expense_in.category, user_id=request.state.user_id)
        crud.add_budget(db, user_id=request.state.user_id, category_id=category.id, monthly_limit=expense_in.monthly_limit)

    expense_obj = crud.add_expense(db=db, expense_in=expense_in, user_id=request.state.user_id)

    category_monthly_limit, category_total_amount_spent = crud.get_category_limit_status(db, user_id=request.state.user_id, category_id=category.id, category_name=expense_in.category)
    email_body = f'Limit Exceeded!!! \nYour limit was {category_monthly_limit} and you have spent {category_total_amount_spent}' if category_monthly_limit <= category_total_amount_spent else f'Currently you can spend {category_monthly_limit - category_total_amount_spent} in {expense_in.category}'
    email.send_email(
        email=request.state.email,
        subject="XpenseMeter Alert",
        body=email_body
    )
    
    return expense_obj