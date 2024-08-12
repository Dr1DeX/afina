install:
	poetry add ${LIB}

remove:
	poetry remove ${LIB}

migrate-create:
	alembic revision --autogenerate -m ${MIGRATION}

migrate-apply:
	alembic upgrade head
