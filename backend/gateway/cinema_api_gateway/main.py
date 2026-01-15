from cinema_helpers.api.health import add_health_check
from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


app = FastAPI(
    title="Cinema API Gateway",
    version="0.0.1",
)


# @app.get("/health")
# def health() -> HealthResponse:
#     return HealthResponse(status="ok")

add_health_check(app=app, service="gateway", version="0.0.0", status="ok", branch=None, commit=None)
