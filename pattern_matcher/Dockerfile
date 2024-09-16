# Build stage
FROM python:3.11-slim as builder

WORKDIR /build
COPY . .
RUN pip install poetry
RUN poetry build

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install dist/*.whl

# Deployment stage
FROM python:3.11-slim as deploy
WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./resource/stix/bundles/ resource/stix/bundles
ENTRYPOINT ["python", "-m", "patternmatcher.main"]
