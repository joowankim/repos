web: gunicorn myapp.wsgi --log-file -
migrate: python manage.py migrate --settings=myapp.settings.production
seed: python manage.py loaddata myapp/item/fixtures/ingredient-data-refined.json myapp/item/fixtures/item-data-refined.json