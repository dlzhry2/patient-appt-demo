FROM python:3.13-slim

RUN pip install poetry==2.1.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/var/cache/pypoetry

WORKDIR /app/panda-app

COPY pyproject.toml poetry.lock ./

# TODO - once dev requirements added, will need to ignore
RUN apt-get update
RUN apt-get install -y libpq-dev gcc
RUN poetry install

COPY api ./api

ENTRYPOINT ["poetry", "run", "python", "-m", "fastapi", "run", "api/main.py"]
