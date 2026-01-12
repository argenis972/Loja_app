# 🛍️ Loja App — Python Backend (Learning Lab) for Financial Business Rules

![CI](https://github.com/argenis972/Loja_app/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?style=flat&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automated%20Tests-brightgreen?style=flat)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-336791?style=flat&logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

> **Branch note:** this README reflects the structure and features of the **`Criar_PostgreSQL`** branch.  
> **Scope note:** this is a **learning/lab project** (not a production-ready system).

---

## 📌 Overview

**Loja App** is a **Python backend lab** focused on practicing:

- installment payment calculation (with constraints)
- receipt persistence (**PostgreSQL**)
- separation of domain rules from I/O (CLI + API)

---

## 🧱 Architecture (no magic, just separation)

- **domain/**: pure rules and entities
- **services/**: use cases
- **infrastructure/**: DB/persistence details
- **ui/** and **api/**: adapters over the same core

### Current repository structure (`Criar_PostgreSQL`)

```text
Loja_app/
├── .github/
│   └── workflows/
|        ├── ci.yml
|        ├── python-app.yml
│        └── tests.yml                 # CI pipeline (GitHub Actions)
|                 
├── alembic/                           # Database migrations (Alembic)
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│
├── api/                               # REST API (FastAPI)
│   ├── main.py                        # FastAPI app
│   ├── pagamentos_api.py              # routes/endpoints
│   ├── deps.py                        # DI (Postgres-only repository)
│   └── dtos/                          # Pydantic models (DTOs)
│
├── config/                            # External configuration
│   ├── settings.py
│   └── taxas.json                     # interest rates table (configurable)
│
├── domain/                            # Pure business core
│   ├── calculadora.py                 # financial calculation engine
│   ├── exceptions.py
│   └── recibo.py                      # domain entity
│
├── services/                          # Use cases
│   ├── pagamento_service.py
│   └── recibo_repository.py
│
├── infrastructure/                    # Technical infrastructure (DB, persistence)
│   ├── __init__.py
│   ├── database.py                    # SQLAlchemy session/engine + DATABASE_URL resolution
│   ├── models.py                      # compatibility module (if kept) / public re-exports
│   ├── storage.py                     # PostgresReciboRepository
|   ├── storage_cli.py                 # CLI-specific repository impl (if kept)
│   └── db/
│       ├── base.py
|       ├── postgres.py
│       ├── mappers/
│       └── models/
│
├── tests/                             # test suite (Postgres + Alembic)
│   └── conftest.py                    # migrates + truncates between tests
│
├── ui/                                # CLI
│   ├── menu.py
│   └── validacoes.py
│
├── alembic.ini
├── setup_database.py
├── main.py                            # CLI entrypoint
├── requirements.txt
├── IMPLEMENTATION_SUMMARY.md
├── .flake8
├── .pre-commit-config.yaml
├── .gitignore
└── README.md
```

---

## 🧮 Business Rules

| Payment Mode        | Condition         | Applied Rule                      |
| ------------------- | ----------------- | --------------------------------- |
| Cash (Upfront)      | immediate payment | 10% discount                      |
| Card (Upfront)      | immediate payment | 5% discount                       |
| Short Installments  | 2x to 6x          | 0% interest (original price)      |
| Long Installments   | 12x to 24x        | fixed 10% increase over the total |

**Validation:** installment attempts outside allowed ranges (e.g., 7x to 11x) must raise a domain validation error.

---

## 🛠️ Setup & Run

Requirements: **Python 3.12+**

```bash
git clone https://github.com/argenis972/Loja_app.git
cd Loja_app
git checkout Criar_PostgreSQL

python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

> `requirements.txt` is intentionally simple for this lab: it may include runtime + dev/test tools together (not a strict prod-only list nor a lockfile).

---

## 🗄️ PostgreSQL (Persistence)

### 1) Create database
```sql
CREATE DATABASE loja_db;
CREATE DATABASE loja_test_db;
```

### 2) Configure `DATABASE_URL`

**Windows (PowerShell):**
```powershell
$env:DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/loja_db"
```

**Linux/Mac:**
```bash
export DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/loja_db"
```

### 3) Run migrations (recommended)
```bash
alembic upgrade head
```

---

## ▶️ Run CLI

```bash
python main.py
```

> The CLI uses the same core rules/services and persists receipts in Postgres.

---

## 🌐 Run REST API (FastAPI)

```bash
uvicorn api.main:app --reload --no-use-colors
```

- Swagger UI: http://127.0.0.1:8000/docs

---

## 🧪 Run tests (Postgres + Alembic)

Tests expect `DATABASE_URL` to point to a **test database**:

**Windows (PowerShell):**
```powershell
$env:DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/loja_test_db"
pytest
```

**Linux/Mac:**
```bash
export DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/loja_test_db"
pytest
```

---

## 📡 API Examples

### ✅ Happy path (example)

`POST /pagamentos/`

```json
{
  "opcao": 3,
  "valor": 100.00,
  "num_parcelas": 6
}
```

```json
{
  "total": 100.00,
  "valor_parcela": 16.67,
  "num_parcelas": 6,
  "taxas": "0% (Sem juros)",
  "status": "aprovado"
}
```

### ❌ Error: invalid installments

```json
{
  "opcao": 3,
  "valor": 100.00,
  "num_parcelas": 10
}
```

```json
{
  "detail": "Número de parcelas inválido: permitido 2 a 6 ou 12 a 24."
}
```

---

## 🧠 CI Root Cause & Fix (DATABASE_URL at import time)

### Root cause
The project validates DB configuration **at import time** (module import).  
In GitHub Actions, `DATABASE_URL` is not defined by default.

**Failure mechanics:**
- `pytest` loads `tests/conftest.py`
- which imports the FastAPI app (`api.main`)
- which imports `infrastructure/database.py`
- which evaluates `_get_database_url()`
- and raises a fatal `RuntimeError` before tests start if `DATABASE_URL` is missing.

### Fix
The initialization became **context-aware**:
- It detects automation/testing contexts (e.g., `PYTEST_CURRENT_TEST` and `GITHUB_ACTIONS`)
- When detected and `DATABASE_URL` is missing, it uses a safe default test URL (instead of crashing)
- The `RuntimeError` remains for real/runtime environments to prevent starting without DB configuration

> This is intentionally kept simple as a lab approach.

---

## 🗺️ Status (Project close)

| Area | Item | Status |
| --- | --- | --- |
| Core | Installment rules + validation | ✅ Done |
| API | FastAPI endpoints | ✅ Done |
| Persistence | PostgreSQL + migrations (Alembic) | ✅ Done |
| Tests | Pytest + CI | ✅ Done |

---

## 👤 Author

**Argenis López**

- LinkedIn: https://www.linkedin.com/in/argenis972/
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

---

## 📜 License

MIT — feel free to study, adapt and evolve.