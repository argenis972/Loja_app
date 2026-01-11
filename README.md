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
- receipt persistence (file/DB)
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

> Note: this branch contains both `infra/` and `infrastructure/`.  
> `infrastructure/` is the main place for DB-related code.

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

```bash
# Linux/Mac
export DATABASE_URL="postgresql://user:password@localhost:5432/loja_app"

# Windows (PowerShell)
$env:DATABASE_URL="postgresql://user:password@localhost:5432/loja_app"
```

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

- Swagger UI: http://127.0.0.1:8000/docs

---

## 🧪 Run tests

```bash
pytest
```

---

## 📡 API Examples

### ✅ Happy path (example)

`POST /pagamentos`

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

### ❌ Error: negative value

```json
{
  "opcao": 1,
  "valor": -50.0,
  "num_parcelas": 1
}
```

```json
{
  "detail": "Valor deve ser maior que zero."
}
```

### ❌ Error: nonexistent option

```json
{
  "opcao": 99,
  "valor": 100.0,
  "num_parcelas": 1
}
```

```json
{
  "detail": "Opção de pagamento inválida."
}
```

> Note: exact error payloads/status codes depend on how API maps domain exceptions (this is a lab, so these details can evolve).

---

## 🗺️ Roadmap

| Area | Item | Status |
| --- | --- | --- |
| Core | Installment rules + validation | ✅ Done |
| API | FastAPI endpoints | ✅ Done |
| Persistence | PostgreSQL + migrations (Alembic) | ✅ Done |
| Tests | Pytest + CI | ✅ Done |
| Future | Improve domain→API error mapping (status codes + error types) | 🔜 Next |
| Future | Async DB experiments (async SQLAlchemy / asyncpg) | 🔜 Next |
| Future | Auth exploration (JWT / sessions) | 🔜 Next |

---

## 👤 Author

**Argenis López**

- LinkedIn: https://www.linkedin.com/in/argenis972/
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

---

## 📜 License

MIT — feel free to study, adapt and evolve.