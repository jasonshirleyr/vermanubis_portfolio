python setup.py install &&
release: python3 vermanubis_portfolio/manage.py migrate 
web: gunicorn project.wsgi:application --preload --workers 1
