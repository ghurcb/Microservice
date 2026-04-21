FROM python:3.11-alpine

WORKDIR /app

# System dependencies
RUN apk update && apk add --no-cache \
    gcc \
    g++ \
    postgresql-client \
    postgresql-dev \
    musl-dev

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application code
COPY . .

# Non-root user
RUN adduser -D -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:8000/health')" || exit 1

CMD sh -c "python wait-for-db.py && \
           alembic upgrade head && \
           exec uvicorn src.main:app --host 0.0.0.0 --port 8000"
