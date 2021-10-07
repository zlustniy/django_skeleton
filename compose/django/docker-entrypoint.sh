#!/usr/bin/env bash

set -e
cmd="$@"
echo "Starting ... $cmd"

case "$1" in
  gunicorn) /commands/web.sh ;;
  *) exec $@ ;;
esac
