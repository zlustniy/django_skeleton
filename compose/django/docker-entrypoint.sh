#!/usr/bin/env bash

set -e
cmd="$@"
echo "Starting ... $cmd"

if [ "$1" = 'gunicorn' ]; then
  /commands/web.sh
fi

if [ "$1" = 'celery-main' ]; then
  /commands/celery_main.sh
else
  echo "Run command ..."
  exec $cmd
fi
