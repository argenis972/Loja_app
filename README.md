# 🛍️ Loja App — Python Backend (Learning Lab)

![CI](https://github.com/argenis972/Loja_app/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?style=flat&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automated%20Tests-brightgreen?style=flat)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-336791?style=flat&logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

> **Branch note:** This README reflects the structure and features of the `Criar_PostgreSQL` branch. <br>
> **Scope note:** This is a learning / lab project focused on backend architecture, financial logic, and testing.

## 📌 Overview

**Loja App** is a **Python backend learning lab.**

### 1. What it is and what it is for

This project exists to practice and understand:

- backend architecture,
- business rule modeling,
- REST API development,
- database persistence,
- and automated testing.

It is intentionally scoped as a **learning repository**, not a production system.

---

### 2. Why the refactor and removal of local UI / simple `main.py`

Early iterations included a local UI and a simple executable `main.py`.
As the project evolved, the focus shifted toward:
- an **API-first backend**,
- clearer separation of concerns,
- persistence and integration testing.

For that reason, the local UI and direct execution flow were removed to keep the backend clean, explicit, and test-driven.

---

### 3. UI as a possible future frontend

UI concerns are intentionally treated as **external consumers.**

A future UI (web or otherwise) could be developed as a separate frontend project that communicates with this backend exclusively via HTTP, without coupling presentation logic to the core system.

## 🧱 Architecture

The project follows a **layered backend architecture** to ensure separation of concerns and testability:

- `domain/`: Pure business rules and entities (independent of frameworks).
- `services/`: Application use cases and logic orchestration.
- `infrastructure/`: Database implementation and external tools.
- `api/`: REST delivery layer (FastAPI controllers).
- `tests/`: Integration and unit tests.

## 📂 Repository Structure (`Criar_PostgreSQL`)

```text
Loja_app/
├── .github/workflows/         # CI pipelines (GitHub Actions)
│   ├── ci.yml
│   ├── python-app.yml
│   └── tests.yml
│
├── alembic/                   # Database migrations (Alembic)
│   ├── env.py
│   └── versions/
│
├── api/                       # REST API Layer (FastAPI)
│   ├── main.py                # App entry point
│   ├── pagamentos_api.py      # Endpoints
│   ├── deps.py                # Dependency Injection
│   └── dtos/                  # Pydantic DTOs
│
├── config/                    # Configuration
│   ├── settings.py
│   └── taxas.json             # Interest rates definition
│
├── domain/                    # Business Core
│   ├── calculadora.py         # Calculation engine
│   ├── exceptions.py
│   └── recibo.py              # Entities
│
├── services/                  # Use Cases
│   ├── pagamento_service.py
│   └── recibo_repository.py   # Interface definition
│
├── infrastructure/            # Implementation details
│   ├── database.py            # SQLAlchemy setup
│   ├── storage.py             # Repository implementation
│   └── db/                    # ORM Models & Mappers
│
├── tests/                      # Test Suite
│   └── conftest.py             # Fixtures (Migration + Truncate)
│
├── alembic.ini                 # Alembic config
├── CHANGELOG.md                # Changelog file
├── .env                        # Environment variables
├── .env.test                   # Test env vars (not committed)
├── .flake8                     # Linting config
├── .gitignore                  # Git ignore rules
├── .pre-commit-config.yaml     # Pre-commit hooks
├── IMPLEMENTATION_SUMMARY.md   # Implementation notes
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```
## PostgreSQL Implementation Details

## Overview

This branch (`Criar_PostgreSQL`) consolidates the backend as an **API-first system**, with a clean separation between domain, services, infrastructure, and delivery layers. It introduces robust persistence using PostgreSQL and managed migrations.

> **Note:** Earlier CLI experiments (`ui/`) were useful during exploration, but the current focus of this branch is the API and backend core.

---

## 🧮 Business Rules

| Payment Mode | Condition | Applied Rule |
| :--- | :--- | :--- |
| **Cash (Upfront)** | Immediate payment | **10% discount** |
| **Card (Upfront)** | Immediate payment | **5% discount** |
| **Short Installments** | 2x to 6x | **0% interest** (original price) |
| **Long Installments** | 12x to 24x | **Fixed 10% increase** over total |

**Validation:** Installment attempts outside allowed ranges (e.g., 7x to 11x) must raise a domain validation error.

---

## 🛠️ Setup & Run

### Requirements
* Python 3.12+

### Installation

```bash
git clone [https://github.com/argenis972/Loja_app.git](https://github.com/argenis972/Loja_app.git)
cd Loja_app
git checkout Criar_PostgreSQL

# Create virtual environment
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
`requirements.txt` is intentionally simple for this lab and may include runtime and test dependencies together.

---

## 🗄️ PostgreSQL (Persistence)

###  1) Create databases
```sql
CREATE DATABASE loja_db;
CREATE DATABASE loja_test_db;
```
## 2) Configure `DATABASE_URL`

### Windows (PowerShell):
```powershell
$env:DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/loja_db"
```
### Linux / Mac (Bash):
```bash
export DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/loja_db"
```

## 3) Run migrations
```bash
alembic upgrade head
```

## 4) 🌐 Run REST API (FastAPI)

```bash
uvicorn api.main:app --reload --no-use-colors
```
- **Swagger UI: http://127.0.0.1:8000/docs**
## 🧪 Run tests (Postgres + Alembic)
Tests expect `DATABASE_URL` to point to a **test database.**

### Windows (PowerShell):
```powershell
$env:DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/loja_test_db"
pytest
```
### Linux / Mac:
```bash
export DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/loja_test_db"
pytest
```
---

## 📡 API Examples

### ✅ Happy path

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
`POST /pagamentos/`
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

The project validates DB configuration **at import time.**
In CI environments (GitHub Actions), `DATABASE_URL` is not defined by default.

### Fix

Initialization was made **context-aware:**

- CI and test contexts are detected
- a safe default test URL is used when appropriate
- a `RuntimeError` is still raised in real runtime if DB configuration is missing

This keeps the behavior explicit while avoiding CI failures.

---

## 🗺️ Status (branch goal reached)

| Area        | Item                           | Status |
| ----------- | ------------------------------ | ------ |
| Core        | Installment rules + validation | ✅ Done |
| API         | FastAPI endpoints              | ✅ Done |
| Persistence | PostgreSQL + Alembic           | ✅ Done |
| Tests       | Pytest + CI                    | ✅ Done |
---

## 👤 Author

### *Argenis López*

- LinkedIn: **https://www.linkedin.com/in/argenis972/**
- GitHub: **https://github.com/argenis972**
- Email: **argenislopez28708256@gmail.com**
---
## 📜 License
MIT — feel free to study, adapt, and evolve.





