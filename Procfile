python setup.py install &&
release: python vermanubis_portfolio/manage.py migrate
web: cd vermanubis_portfolio && gunicorn vermanubis_portfolio.wsgi:application --log-file - --log-level debug
