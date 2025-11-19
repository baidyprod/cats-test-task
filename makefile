lint:
	black . --line-length 120
	isort .
	ruff check . --fix

check:
	black . --check --line-length 120
	isort . --check-only
	ruff check .