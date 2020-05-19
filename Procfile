python setup.py install &&
release: python vermanubis_portfolio/manage.py migrate
web: web: gunicorn project.wsgi:application --log-file - --log-level debug
