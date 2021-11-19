#!/bin/sh

python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'goodpassword')" | python3 manage.py shell

gunicorn lumiobytenet.wsgi:application --bind 0.0.0.0:8000