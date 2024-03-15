#!/bin/sh
python manage.py migrate;
python manage.py collectstatic --noinput;
python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput;
gunicorn website.wsgi:application --bind 0.0.0.0:8000;