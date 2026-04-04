FROM python:3.8.1-slim as python-base

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]