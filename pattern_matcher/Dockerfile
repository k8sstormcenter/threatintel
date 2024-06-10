# Build stage
FROM python:3.11-slim as builder
WORKDIR /build

COPY pyproject.toml README.md ./
RUN pip install poetry
COPY src ./src

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Deployment stage
FROM python:3.11-slim as deploy
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY src ./src
ENV PYTHONPATH="/app/src:$PYTHONPATH"

CMD ["python", "src/patternmatcher/main.py"]