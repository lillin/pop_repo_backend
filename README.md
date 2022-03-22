## Popular Repository
Service intends to determine whether repository is popular from its stars and forks amount; it gets data from GitHub API. 
Project dockerized and implemented using a such shortlist of technologies:
- [Django 3.2](https://docs.djangoproject.com/en/3.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [GitHub API](https://docs.github.com/en/rest)
- [Swagger OpenAPI](https://swagger.io/docs/specification/about/)
- [Pytest](https://docs.pytest.org/en/7.1.x/) and [pytest-django](https://pytest-django.readthedocs.io/en/latest/) 

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
See Coverage report: `coverage report`

#### Notes
...
