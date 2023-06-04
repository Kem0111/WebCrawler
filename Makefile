install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run pytest

start:
	poetry run start

create_csv_with_results:
	poetry run create-csv

test-cov:
	poetry run pytest --cov-report xml --cov=src tests/