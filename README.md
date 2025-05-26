# patient-appt-demo

The Patient Appointment Network Data Application (**PANDA**) is a CRUD backend app for managing patient data and appointments.

It uses the [FastAPI](https://fastapi.tiangolo.com/) Python-based framework for the API backend and PostgreSQL for the database.

It is currently in development for an initial MVP release.

## How to run
### Pre-requisites
You will need:

(lower versions may work, but this is what it has been tested with)
- Docker  >= v.28.1.1
- [docker-compose](https://docs.docker.com/compose/install/) >= 1.29.2
- You may also want to install pgAdmin for interacting with the database

### Steps
- Create a `.env` file in the root directory and copy the contents of the `.env-example` files to it.
- Define your own values for the DB_* variables.
- Ensure you `source` your new .env file to ensure the variables are available in your terminal.
- Finally, simply run `docker compose up --build`. This will build you an API backend.

### Interacting with the API
Okay, looks like you're all setup. So now what?

Simply navigate to http://localhost:8000/docs#
This documents the API, and you can interact directly from the web page.

Alternatively, you could perform requests against the local endpoint using a tool of your choice such a cURL or Postman.

If you would like to run the application in dev mode, then follow the instructions in the `./panda-app` README.
