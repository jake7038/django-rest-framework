FROM python:3.13-slim as python-base

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

RUN curl -sSl https: //raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]