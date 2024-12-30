from fastapi import APIRouter
from XpenseMeter.api.endpoints import user, expense

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(expense.router, prefix="/expenses", tags=["expenses"])

@api_router.get("/health")
def health_check():
    return {"status": "ok"}