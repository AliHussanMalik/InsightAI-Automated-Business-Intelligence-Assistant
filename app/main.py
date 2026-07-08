from fastapi import FastAPI

from app.api.routes.dataset_routes import router as dataset_router

app = FastAPI(
    title="InsightAI",
    version="0.1.0"
)

app.include_router(dataset_router)


@app.get("/")
def home():
    return {
        "message": "InsightAI API"
    }