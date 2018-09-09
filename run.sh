#!/bin/bash
SERVER_PORT=8080;
echo port is $SERVER_PORT
echo "make migrations"
python3 manage.py makemigrations
echo "migrate"
python3 manage.py migrate
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.io', 'password')" | python3 manage.py shell
echo "from django.contrib.auth.models import User; user=User.objects.create_user('admin', password='admin'); user.is_superuser=True;user.is_staff=True;user.save()" | python3 manage.py shell
echo [$0] Starting Django Server…
python3 manage.py runserver 0.0.0.0:$SERVER_PORT
