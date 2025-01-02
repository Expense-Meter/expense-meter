from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List
from XpenseMeter import schemas, crud
from XpenseMeter.db.session import get_db
from XpenseMeter.decorators.jwt import token_authentication_required
from XpenseMeter.utils import email

router = APIRouter()

@router.get("/current-month", response_model=List[schemas.ExpenseBase])
@token_authentication_required
async def get_monthly_report(request: Request, db: Session = Depends(get_db)):
  return {}