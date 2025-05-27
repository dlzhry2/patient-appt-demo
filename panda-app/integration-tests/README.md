# API integration-tests

This is still TODO.

Given the acceptance criteria, the plan would be to prioritise e2e tests that avoid any mocking and test the full end to end journey.

Pytest would likely be the chosen tool. An environment variable could be provided to indicate to use an in-memory database for the purposes of testing when issuing the `docker compose` command.
