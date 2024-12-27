from fastapi import APIRouter
from XpenseMeter.api.endpoints import user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])

@api_router.get("/health")
def health_check():
    return {"status": "ok"}