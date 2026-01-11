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
<<<<<<< HEAD
├── alembic/             # 🗃️ Migrações de Banco de Dados (se aplicável)
│   ├── versions/
│   ├── env.py
│   ├── Readme.md
│   └── script.py.mako
|
├── api/                 # 🌐 Camada de Entrada (FastAPI)
│   ├── main.py          # Configuração da Aplicação
│   ├── pagamentos_api.py
│   └── dtos/            # Contratos de dados (Pydantic Models)
=======
├── alembic/                           # Database migrations (Alembic)
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
>>>>>>> main
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
<<<<<<< HEAD
├── infra/      # 💾 Detalhes Técnicos
│   └── storage.py       # Implementação de persistência em arquivo
|
├── infrastructure/
|   ├── __init__.py
|   ├── database.py
|   ├── models
|   ├── storage
│   └── db.py/
│         └── postgres.py 
|
├── receipts/            # 📄 Saída de Arquivos (Ignorado pelo Git)
│   └── *.json / *.txt   # Recibos gerados localmente
=======
├── infra/                             # Legacy/local persistence implementation
│   └── storage.py
│
├── infrastructure/                    # Technical infrastructure (DB, persistence)
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── storage.py
│   └── db/
>>>>>>> main
│
├── tests/                             # test suite
├── ui/                                # CLI
│   ├── menu.py
│   └── validacoes.py
│
<<<<<<< HEAD
├── venv/                 # Ambiente Virtual (Ignorado pelo Git)
|
├── .env                  # Variáveis de ambiente (Ignorado pelo Git)
├── .flake8               # Configuração do Flake8
├── .pre-commit-config.yaml  # Configuração do Pre-commit
├── alembic.ini            # Configuração do Alembic
├── IMPLEMENTATION.md      # Documentação Técnica
├── .gitignore
├── setup_database.py     # Script para criação de tabelas no DB
├── main.py              # Entry point (CLI)
├── README.md
└── requirements.txt
=======
├── alembic.ini
├── setup_database.py
├── main.py                            # CLI entrypoint
├── requirements.txt
├── IMPLEMENTATION_SUMMARY.md
├── .flake8
├── .pre-commit-config.yaml
├── .gitignore
└── README.md
>>>>>>> main
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

<<<<<<< HEAD
### 4. Configurar Persistência (Opcional)

O projeto suporta duas formas de persistência de recibos:

#### **Opção A: Arquivo (Padrão)**
Por padrão, os recibos são salvos em arquivo de texto. Não requer configuração adicional.

#### **Opção B: PostgreSQL**
Para usar PostgreSQL, configure a variável de ambiente `DATABASE_URL`:

```bash
# Linux/Mac
export DATABASE_URL="postgresql://usuario:senha@localhost:5432/loja_app"

# Windows (PowerShell)
$env:DATABASE_URL="postgresql://usuario:senha@localhost:5432/loja_app"
```

**Criação do banco de dados:**
```sql
-- Conecte-se ao PostgreSQL e execute:
CREATE DATABASE loja_app;
```

**Criação da tabela:**

As tabelas são criadas automaticamente na inicialização da aplicação. Você também pode executar o script de setup:

```bash
python setup_database.py
```

Ou criar manualmente com SQL:

```sql
CREATE TABLE recibos (
    id SERIAL PRIMARY KEY,
    total FLOAT NOT NULL,
    metodo VARCHAR(50) NOT NULL,
    parcelas INTEGER NOT NULL DEFAULT 1,
    informacoes_adicionais VARCHAR(500) NOT NULL DEFAULT '',
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

**Nota:** Durante testes, o sistema usa SQLite em memória automaticamente, não requerendo PostgreSQL.

### 5. Executar via CLI:
=======
---
>>>>>>> main

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
<<<<<<< HEAD
### 6. Executar a API REST (FastAPI)
=======
>>>>>>> main

---

## 🌐 Run REST API (FastAPI)

```bash
uvicorn api.main:app --reload
```

Swagger UI:

<<<<<<< HEAD
### 7. Executar os testes automatizados

```bash
pytest
```

Status atual:

- ✅ 100% dos testes passando

### 📡 Exemplo de Uso da API
=======
- http://127.0.0.1:8000/docs
>>>>>>> main

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

<<<<<<< HEAD
## 🗺️ **Roadmap de Evolução**
=======
---

## 🗺️ Roadmap

| Feature                                     | Status      |
| ------------------------------------------- | ----------- |
| Automated tests (pytest)                    | ✅ Done      |
| REST API with FastAPI                       | ✅ Done      |
| External configuration (rates table)         | ✅ Done      |
| PostgreSQL persistence                       | ✅ Done      |
| Alembic migrations                           | ✅ Done      |
>>>>>>> main

---

## 👤 Author

<<<<<<< HEAD
| Feature                                   | Status          |
| ----------------------------------------- | --------------- |
| Testes automatizados com pytest           | ✅ **Concluído**     |
| API REST com FastAPI                      | ✅ **Concluído**     |
| Configuração externa (taxas)              | ✅ **Concluído**     |
| Persistência em banco (SQLite/PostgreSQL) | ✅ **Concluído** |

## 🧠 Filosofia do Projeto

- **Evolutividade:** Código pensado para manutenção a longo prazo, não apenas execução pontual.
- **Simplicidade:** Evitar complexidade acidental; usar a ferramenta certa para o trabalho.
- **Consistência:** A regra de negócio é a verdade única, independente da interface (CLI ou API).

## 👤 Autor 

**Argenis López** <br />

*Backend Developer — Python.*

## 📬 Contato
=======
**Argenis López**
>>>>>>> main

- LinkedIn: https://www.linkedin.com/in/argenis972/
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

---

## 📜 License

MIT — feel free to study, adapt and evolve.