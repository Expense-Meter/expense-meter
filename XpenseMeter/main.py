from fastapi import FastAPI
from XpenseMeter.routes.expense_routes import router as expense_router
from XpenseMeter.routes.user_auth_routes import router as user_router
from XpenseMeter.routes.report_routes import router as report_router
app = FastAPI()

app.include_router(expense_router)
app.include_router(user_router)
app.include_router(report_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
