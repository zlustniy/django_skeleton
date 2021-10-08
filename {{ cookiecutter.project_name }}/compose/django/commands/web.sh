#!/usr/bin/env bash

python manage.py migrate --noinput
gunicorn {{ cookiecutter.project_name }}.wsgi -b 0.0.0.0:${DJANGO_PORT:-5000} --pid /var/run/gunicorn.pid -w ${GUNICORN_WORKERS:-1}