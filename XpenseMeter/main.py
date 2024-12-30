from fastapi import FastAPI
from XpenseMeter.routes.report_routes import router as report_router
from XpenseMeter.api import api_router

app = FastAPI()


app.include_router(api_router)
app.include_router(report_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
