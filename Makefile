run:
	python3.10 src/main.py

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 pytest -vv
