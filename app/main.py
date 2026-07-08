from fastapi import FastAPI

app = FastAPI(
    title="insights",
    description="AI Powered Business Analytics Platform",
    version = "1.0.0"
)

@app.get("/")
def home():
    return{
        "message": "InsightAI API is running"
    }