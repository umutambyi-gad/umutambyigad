release: python manage.py migrate
web: gunicorn umutambyigad.wsgi --log-file -