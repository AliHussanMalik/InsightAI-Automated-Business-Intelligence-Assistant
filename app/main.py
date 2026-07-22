from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.dataset_routes import router as dataset_router

app = FastAPI(
    title="InsightAI",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dataset_router)


@app.get("/")
def home():
    return {
        "message": "InsightAI API"
    }