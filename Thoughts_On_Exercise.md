# Thoughts on the coding exercise
Overall, I quite enjoyed it. Was certainly fun getting back into FastAPI having not used it for a little while (it has moved on a lot).
The task was nicely open-ended in terms of being able to choose which tech to use, and required a good amount of up front thinking about design and prioritisation.

Given the project brief I prioritised, above all, having a fully Dockerised end-to-end stack with a backend and a database that would be easy for developers to run. Even with LLMs it can be a bit overwhelming getting all the boilerplate setup to a good standard and interacting properly.

I'm glad I looked into this first and am pleased with the end result, though it did take a little while getting started before I could work on the API code. I initially timeboxed the full task to 2-3 hours but ended up taking double that, if I'm honest, as I wanted to complete all interactions for at least one endpoint!

Please refer to the `TODO.txt` file for a vaguely prioritised list of features and technical improvements that I would next work on given more time.

# Tech choices - rationale

Some key considerations for the task were:
- The client wants to avoid vendor lock-in and use smaller frameworks
- They have not yet selected their database technology and would like to be as agnostic as possible
- Would like to be able to perform data analysis and be able to answer queries such as how many appointments were missed, broken down by clinician, department etc.
- The PANDA currently doesn't contain much data about clinicians, but will eventually track data about the specific organisations they currently work for and where they work from

## Database layer
`postgreSQL` was chosen. I decided to opt for a relational database given the client's requirement around data analysis. Although this could also be met using a DocumentDB, an SQL DB would be more suited to the kinds of analytical queries they would want to perform.

The structure of the data also corresponded well to a relational design i.e having a separate `patients` table and an `appointments` table with a FK relationship to `patients`. This would also suit the future requirements around storing more data to do with clinicians, while a `departments` table would likely also be required.

Finally, the use of the `SQL Alchemy` ORM means that any other SQL database could be easily used. There is no tight coupling to postgres and the use of a repository pattern makes it even easier to switch the db layer technology. Postgres was simply chosen at this point as it is open source.

## Backend layer
`Fast API` was chosen as it is lightweight, open-source and Python is widely used in the healthcare domain.

`SQL Alchemy` ORM was used alongside it for database interactions as it is agnostic of the underlying DB technology used.

### Some notes on coming back to FastAPI
As mentioned I had not used FastAPI for a little while and it was interesting coming back to it having done a few recent projects using Java SpringBoot and C# .NET Web API.

The last large project I worked on was interacting directly with the starlette request object and was using custom JSON schema validation rather than pydantic.

Since the client requirement was only for JSON to be returned I have omitted a `/port` or `/handler` layer since we only have one proposed request/response format for the API. Overall, there was a bit of reading to do to get up to speed as I had not used pydantic and SQl ALchemy before, but I found them really easy to work with. Request validation was pretty seamless with pydantic and I really enjoyed using it!
