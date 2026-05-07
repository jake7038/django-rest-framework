#!/bin/bash
python manage.py migrate auth --noinput
python manage.py migrate contenttypes --noinput
python manage.py migrate admin --noinput
python manage.py migrate sessions --noinput
python manage.py migrate authtoken --noinput
python manage.py migrate product --noinput
python manage.py migrate order --noinput
python manage.py collectstatic --noinput
gunicorn bookstore.wsgi:application --bind 0.0.0.0:8000
