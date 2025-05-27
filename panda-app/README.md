# panda-app

## Overview
This is a FastAPI backend project for managing patient data and appointments.
SQL Alchemy 2.0 ORM is used for interacting with the database layer.

It aims to keep the business logic in the `./service` layer decoupled from hard dependencies on particular technology/frameworks.
There is also the `./repository` layer which abstracts the database interactions to enable easier transition to other storage options, if ever requiired.

Finally, the `openapi.json` file documents how to interact with the API.

## How to run
### Pre requisites
- Python >= 3.13
- Poetry >= 2.1.3
- libpq-dev gcc installed with your package manager. E.g. if you are using apt then run `apt-get install -y libpq-dev gcc`

### Steps
- As we are going to run FastAPI in dev mode, we will first want to start the database.
- Ensure you have sourced the .env variables as per the root README
- From the root of the project run `docker compose up db --build`
- Then navigate to the `./panda-app` directory
- Run `poetry install`
- Finally run `poetry run fastapi dev api/main.py`
