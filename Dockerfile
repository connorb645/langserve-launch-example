FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install poetry && \
 poetry config virtualenvs.create false && \
 poetry install --no-interaction --no-ansi --only main

CMD poetry run uvicorn learn_map.server:app --host 0.0.0.0 --port $PORT
