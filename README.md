# 🛍️ Loja App — Python Backend for Financial Business Rules

![CI](https://github.com/argenis972/Loja_app/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?style=flat&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automated%20Tests-brightgreen?style=flat)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-336791?style=flat&logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

> **Branch note:** this README reflects the structure and features of the **`Criar_PostgreSQL`** branch.

---

## 📌 Overview

**Loja App** is a **Python backend project focused on financial business rules**, especially installment payment calculation and receipt persistence.

Key goals:

- **Business rules first**: domain logic is isolated from frameworks and I/O.
- **Layered architecture**: domain / services / infrastructure (and adapters).
- **Multiple entrypoints**: CLI + REST API sharing the same core domain.
- **Automated tests + CI**: fast feedback and regression safety.

---

## 🧠 Project Evolution

1. **MVP (v1):** initial payment calculation via a simple CLI.
2. **Business Rules:** introduced installment rules + conditional discounts.
3. **Refactor (v2):** moved to a layered architecture and decoupled components.
4. **Production-ready direction (current):** FastAPI REST + persistence with PostgreSQL + CI.

---

## 🧱 Architecture (no magic, just separation)

The project is inspired by **Clean Architecture / Hexagonal** principles:

- The **domain** does not depend on frameworks, databases, or UI.
- **services** orchestrate use cases.
- **infrastructure** implements technical details (database, persistence).
- **CLI/API** are adapters that consume the same domain and services.

### Current repository structure (`Criar_PostgreSQL`)

```text
Loja_app/
├── .github/
│   └── workflows/
│       └── tests.yml                  # CI pipeline (GitHub Actions)
│
├── alembic/                           # Database migrations (Alembic)
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│
├── api/                               # REST API (FastAPI)
│   ├── main.py                        # FastAPI app
│   ├── pagamentos_api.py              # routes/endpoints
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
├── infra/                             # Legacy/local persistence implementation
│   └── storage.py
│
├── infrastructure/                    # Technical infrastructure (DB, persistence)
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── storage.py
│   └── db/
│
├── tests/                             # test suite
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

> Note on naming: this branch currently contains both `infra/` and `infrastructure/`.  
> `infrastructure/` is the main place for DB-related code; `infra/` still exists in the repo and is documented accordingly.

---

## 🧮 Business Rules (explicit by design)

| Payment Mode        | Condition         | Applied Rule                         |
| ------------------- | ----------------- | ------------------------------------ |
| Cash (Upfront)      | immediate payment | 10% discount                         |
| Card (Upfront)      | immediate payment | 5% discount                          |
| Short Installments  | 2x to 6x          | 0% interest (original price)         |
| Long Installments   | 12x to 24x        | fixed 10% increase over the total    |

**⚠️ Validation:** installment attempts outside the allowed ranges (e.g., 7x to 11x) must raise a domain validation error.

---

## 🛠️ Setup & Run

Requirements: **Python 3.12+**

### 1) Clone and checkout this branch

```bash
git clone https://github.com/argenis972/Loja_app.git
cd Loja_app
git checkout Criar_PostgreSQL
```

### 2) Create and activate a virtualenv

```bash
python -m venv venv

# Windows:
.\venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ PostgreSQL (Persistence)

Configure:

```bash
# Linux/Mac
export DATABASE_URL="postgresql://user:password@localhost:5432/loja_app"

# Windows (PowerShell)
$env:DATABASE_URL="postgresql://user:password@localhost:5432/loja_app"
```

Create the database:

```sql
CREATE DATABASE loja_app;
```

### Option A (recommended): Alembic migrations

```bash
alembic upgrade head
```

### Option B: setup script

```bash
python setup_database.py
```

---

## ▶️ Run CLI

```bash
python main.py
```

---

## 🌐 Run REST API (FastAPI)

```bash
uvicorn api.main:app --reload
```

Swagger UI:

- http://127.0.0.1:8000/docs

---

## 🧪 Run tests

```bash
pytest
```

---

## 📡 API Example

**Endpoint**: `POST /pagamentos`

**Request**
```json
{
  "opcao": 3,
  "valor": 100.00,
  "num_parcelas": 6
}
```

**Response (example)**
```json
{
  "total": 100.00,
  "valor_parcela": 16.67,
  "num_parcelas": 6,
  "taxas": "0% (Sem juros)",
  "status": "aprovado"
}
```

---

## 🗺️ Roadmap

| Feature                                     | Status      |
| ------------------------------------------- | ----------- |
| Automated tests (pytest)                    | ✅ Done      |
| REST API with FastAPI                       | ✅ Done      |
| External configuration (rates table)         | ✅ Done      |
| PostgreSQL persistence                       | ✅ Done      |
| Alembic migrations                           | ✅ Done      |

---

## 👤 Author

**Argenis López**

- LinkedIn: https://www.linkedin.com/in/argenis972/
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

---

## 📜 License

MIT — feel free to study, adapt and evolve.