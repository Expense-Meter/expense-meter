from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List
from XpenseMeter import schemas, crud
from XpenseMeter.db.session import get_db
from XpenseMeter.decorators.jwt import token_authentication_required

router = APIRouter()

@router.get("/", response_model=List[schemas.ExpenseBase])
@token_authentication_required
async def read_expenses(request: Request, email: str = None, db: Session = Depends(get_db)):
    """
    Retrieve all expenses.
    """
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email query parameter is required",
        )
    user = crud.get_user_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not registered",
        )
    return crud.get_current_month_expenses(db, user_id=user.id)