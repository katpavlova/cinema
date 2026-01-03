from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class HealthResponse(BaseModel):
    status: str


app = FastAPI(
    title="Cinema API Gateway",
    version="0.0.1",
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")



