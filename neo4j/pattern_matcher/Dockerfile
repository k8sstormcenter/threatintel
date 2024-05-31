# TODO: split into build & deploy phase
FROM python:3.11-slim
WORKDIR /app
# RUN python -m pip install click neo4j 'aiokafka[snappy]' stix2-matcher==3.0.0 stix2-patterns==2.0.0
COPY . .
RUN python -m pip install .
CMD ["python", "-m", "src.main"]
