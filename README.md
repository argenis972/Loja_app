# Loja_app

A simple store ("Loja") web API project.

## Repository tree

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── utils/
├── infrastructure/
│   ├── models.py
│   └── storage.py
├── migrations/
├── docs/
├── requirements.txt
└── README.md
```

## Documentation

See: **/docs** (Swagger UI / OpenAPI).

## Database migrations (Alembic)

This project uses **Alembic** to manage database schema migrations.

- Generate a new migration:
  ```bash
  alembic revision --autogenerate -m "your message"
  ```
- Apply migrations:
  ```bash
  alembic upgrade head
  ```

## Infrastructure

The `infrastructure/` package contains persistence and database-related code.

- `infrastructure/models.py`: SQLAlchemy models mapped to the database.
- `infrastructure/storage.py`: database/session helpers and storage utilities.

## Roadmap

| Status | Item |
|---|---|
| ✅ Done | Basic API structure |
| ✅ Done | CRUD for products |
| 🔄 In progress | PostgreSQL integration |
| ⏳ Planned | Authentication (JWT) |
| ⏳ Planned | Tests and CI |

## Author

- **Argenis Gonzalez**
- GitHub: https://github.com/argenis972
- Email: argenisgonzalez@gmail.com
