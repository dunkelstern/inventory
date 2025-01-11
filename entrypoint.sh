#!/bin/sh

cd /usr/src/app

# poetry run python manage.py collectstatic --noinput
poetry run python manage.py migrate --noinput

exec poetry run gunicorn inventory_project.wsgi -b 0.0.0.0:8000