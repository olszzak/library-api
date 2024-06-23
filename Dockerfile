FROM python:3.11 as builder


WORKDIR /app

RUN pip install -U pip

COPY requirements.in .
RUN pip install --root /install -r requirements.in wait-for-it


FROM python:3.11-slim as runtime

COPY --from=builder /install /

COPY app app
COPY alembic alembic
COPY alembic.ini alembic.ini

ENV PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV PORT=8000 \
    LOG_LEVEL="info"

CMD ["uvicorn", "app.main:create_app"]
