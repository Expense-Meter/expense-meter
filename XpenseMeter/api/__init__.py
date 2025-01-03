from fastapi import APIRouter
from XpenseMeter.api.endpoints import user, expense, report

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(expense.router, prefix="/expenses", tags=["expenses"])
api_router.include_router(report.router, prefix="/reports", tags=["reports"])

@api_router.get("/")
def read_root():
    return {"message": "Welcome to XpenseMeter"}

@api_router.get("/health")
def health_check():
    return {"status": "ok"}