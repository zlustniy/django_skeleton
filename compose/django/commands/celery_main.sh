#!/usr/bin/env bash

set -e

celery -A cookiecutter_project_name worker \
  --loglevel=error \
  --queues=celery,emails \
  --concurrency=${CONCURRENCY:-1} \
  --hostname=main \
  --events \
  --without-gossip \
  --without-mingle \
  --without-heartbeat
