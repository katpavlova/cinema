from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field


class HealthCheck(BaseModel):
    version: str = Field(description='')
    status: str = Field(description='')
    service: str = Field(description='')
    commit: str | None = Field(description='')
    branch: str | None = Field(description='')


def add_health_check(
        app: FastAPI,
        service: str,
        version: str,
        status: str,
        branch: str | None = None,
        commit: str | None = None,
) -> None:
    """
    Добавление healthcheck роутера GET /health/
    :param app: объект FastAPI
    :param service: название сервиса
    :param version: версия
    :param branch: ветка
    :param commit: коммит
    :param status: статус
    """
    router = APIRouter(prefix="/health", tags=["HealthCheck"])

    @router.get("/", response_model=HealthCheck)
    def health_check() -> HealthCheck:
        """
        Запрос здоровья
        """
        return HealthCheck(
            version=version,
            service=service,
            branch=branch,
            commit=commit,
            status=status,
        )

    app.include_router(router)