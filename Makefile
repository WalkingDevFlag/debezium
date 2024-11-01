build:
	docker build -t debezium_tester_app .

up:
	docker compose up -d

linter:
	uv run ruff check . --fix && uv run ruff format --check .

format:
	uv run ruff format .