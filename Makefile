shell:
	pipenv run python manage.py shell

s:
	pipenv run python manage.py runserver

makemigrations:
	pipenv run python manage.py makemigrations

migrate:
	pipenv run python manage.py migrate
