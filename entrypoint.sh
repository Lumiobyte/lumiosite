#!/bin/sh

python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'evanpartridge0@gmail.com', 'goodpassword')" | python3 manage.py shell

chown www-data db.sqlite3

gunicorn lumiobytenet.wsgi:application --bind 0.0.0.0:8000