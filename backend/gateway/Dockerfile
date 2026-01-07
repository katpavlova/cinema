FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --only main --no-root

COPY cinema_api_gateway/ /app/cinema_api_gateway/

CMD ["/app/.venv/bin/uvicorn", "cinema_api_gateway.main:app", "--host", "0.0.0.0", "--port", "11101"]
