python setup.py install &&
release: python manage.py migrate
web: gunicorn vermanubis_portfolio.wsgi --log-file -
