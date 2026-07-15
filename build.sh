#!/usr/bin/env bash
uv sync --frozen
uv run manage.py collectstatic --noinput
uv run manage.py migrate
if [[ $CREATE_SUPERUSER ]];
then
  uv run manage.py createsuperuser --no-input
fi
