## Popular Repository
Service intends to determine whether repository is popular from its stars and forks amount; it gets data from GitHub API. 
Project dockerized and implemented using a such shortlist of technologies:
- [Django 3.2](https://docs.djangoproject.com/en/3.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [GitHub API](https://docs.github.com/en/rest)
- [Swagger OpenAPI](https://swagger.io/docs/specification/about/)
- [Pytest](https://docs.pytest.org/en/7.1.x/) and [pytest-django](https://pytest-django.readthedocs.io/en/latest/) 

There are two endpoints:
- To get information by the search by the repository name only because GitHub have a greate number of eponymous repositories.
- To get information by specifying an owner near the repository name to get a particular repo.

Search API assumes pagination-like feature due to the great number of results (for some queries it was hundreds of thousands) which directly affects response time.
Pagination wasn't implemented using built-in DRF paginators (it looks like overkill to implement custom as the default ones assume interaction with querysets) and uses value returned by GitHub API.

#### Table of content
* [Requirements](#requirements)
* [Setup on local machine](#setup-on-local-machine)
* [Run tests](#run-tests)
* [Notes](#notes)

#### Requirements
- Python 3.9
- Docker
- docker-compose

#### Setup on local machine
Project can be run as a container using docker-compose or by setup of virtual environment.<br>
_To run project using Docker:_
- Install [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/)
- Create `.env` file in project's root directory and provide variables from `.env.example`
- Make sure if port `8000` is available
- Run `docker-compose up` from project's root

If `requirements.txt` was updated, run `docker-compose build` to install new libraries.
<br>

_To run project using virtual environment:_
- Create & activate virtual environment (i.e. [venv](https://docs.python.org/3.9/library/venv.html))
- Run `pip install -r requirements.txt`
- Run `python manage.py migrate` to apply DB migrations
- Run `python manage.py runserver` to start server

Go to `http://localhost:8000/docs/` to meet API documentation

#### Run tests
Tests located in `api/tests` directory.

Run tests with Coverage: `coverage run -m pytest -vv`<br>
See Coverage report: `coverage report -m`

#### Notes
For GitHub authentication was used personal token instead of an application registration (which requires app deployment), but for commercial projects it's inappropriate.

CORS management is nice to have as static files can be served e.g. on AWS s3 bucket, but not within project.

If we want to run project on a single instance, HTTP server and WSGI interface are likely to be configured, so for dockerized project we'd need an extra container for HTTP server e.g. Nginx.

There are unit tests, so GitHub action to run them before PR merge to master is nice to have. Also, views should be covered as well.
It's a good practice to add versioning for API and for project as well.
