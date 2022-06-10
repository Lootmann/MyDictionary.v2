run:
	python3.10 src/main.py

arg:
	python3.10 src/main.py hello

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 pytest -s -vv
