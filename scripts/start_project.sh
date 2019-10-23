#!/bin/sh

# Shell script to start the Django Project

# To run Django project 'manage' commands in the container:
#   Run 'docker-compose run project python /wrkdir/project/manage.py [command]'

# Set current directory to script directory
cd "$(dirname "$0")"
. ../.env

echo "Starting Django Project $PROJECT_NAME"

python /$PROJECT_WORK_DIR/$PROJECT_NAME/manage.py collectstatic --noinput
python /$PROJECT_WORK_DIR/$PROJECT_NAME/manage.py migrate --noinput

if [ "$DEVELOPMENT" = "True" ]
then
  # For dev, to have reload
  echo "Running in DEV mode."
  python /$PROJECT_WORK_DIR/$PROJECT_NAME/manage.py runserver 0.0.0.0:$WSGI_PORT
else
    echo "Running in PROD mode."
    gunicorn --chdir /$PROJECT_WORK_DIR/$PROJECT_NAME --bind 0.0.0.0:$WSGI_PORT  $PROJECT_NAME.wsgi:application
fi
