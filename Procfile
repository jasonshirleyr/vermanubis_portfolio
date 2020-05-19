python setup.py install &&
release: python vermanubis_portfolio/manage.py migrate
web: gunicorn vermanubis_portfolio/vermanubis_portfolio.wsgi --log-file -
