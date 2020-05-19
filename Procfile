python setup.py install &&
release: python3 vermanubis_portfolio/manage.py makemigrations && python3 vermanubis_portfolio/manage.py migrate 
web: gunicorn vermanubis_portfolio.wsgi --log-file -
