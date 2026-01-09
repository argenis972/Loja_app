# 🛍️ Loja App — Backend Python para Regras de Pagamento

![CI](https://github.com/argenis972/Loja_app/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?style=flat&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testes%20Automatizados-brightgreen?style=flat)
![Status](https://img.shields.io/badge/Status-Estável-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Visão Geral

**Loja App** é um **projeto backend em Python focado na modelagem e evolução de regras de negócio financeiras**, especialmente no cálculo de pagamentos parcelados e geração de recibos.

> Projeto desenvolvido com foco em boas práticas de engenharia de software,
> simulando regras reais de pagamento utilizadas em sistemas comerciais de varejo.

* **Clareza das regras de negócio:** Lógica financeira desacoplada da interface.
* **Clean Architecture:** Separação estrita entre Domínio, Serviços e Infraestrutura.
* **Testabilidade:** Cobertura de testes unitários e de integração.
* **Qualidade de código:** Padrões rigorosos de linting e formatação.

---

## 🛡️ Qualidade de Código

Este projeto segue padrões rigorosos de desenvolvimento Python moderno:

* **Black:** Formatação de código intransigente.
* **Isort:** Organização automática de importações.
* **Flake8:** Análise estática para detecção de erros de estilo e lógica.
* **Pre-commit:** Hooks ativos para garantir consistência antes de cada commit.

---

## 🧠 Evolução do Projeto

1.  **MVP (v1):** Implementação inicial de cálculos via CLI simples.
2.  **Regras de Negócio:** Introdução de lógica de parcelamento e descontos condicionais.
3.  **Refatoração (v2):** Adoção de arquitetura em camadas e desacoplamento.
4.  **Profissionalização (Atual):** API REST (FastAPI), CLI refinada e testes automatizados (CI/CD).

---

## 🧱 Arquitetura do Projeto

A arquitetura é modular, inspirada em **Clean Architecture / Hexagonal**. As regras de negócio (Domínio) não dependem de frameworks, I/O ou infraestrutura externa.

```text
Loja_app/
├── .github/
│   └── workflows/
│       └── tests.yml    # 🤖 Pipeline de CI (GitHub Actions)
│
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
│
├── config/              # ⚙️ Configurações Externas
│   ├── settings.py
│   └── taxas.json       # Tabela de juros parametrizável
│
├── domain/              # 🧠 Core Business (Puro Python)
│   ├── exceptions.py
│   ├── recibo.py        # Entidade de Domínio
│   └── calculadora.py   # Motor de cálculo financeiro
│
├── services/            # ⚙️ Casos de Uso
│   ├── pagamento_service.py
│   └── recibo_repository.py
│
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
│
├── tests/               # 🧪 Suíte de Testes
│   ├── test_calculadora.py
│   ├── test_recibo.py
│   └── ...
│
├── ui/                  # 🖥️ Interface de Usuário (CLI)
│   ├── menu.py
│   └── validacoes.py
│
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
```
## 🚀 Destaques Técnicos

### API REST (FastAPI)

- Endpoints otimizados para cálculo de pagamentos e emissão de recibos.
- Validação de dados automática com Pydantic.
- Documentação interativa nativa (Swagger UI).

### CLI Profissional

- Design visual aprimorado com caracteres box-drawing (╔═╗).
- Formatação monetária (R$) e alinhamento tabular.
- Reutilização do mesmo core domain da API, garantindo consistência.

### Testes Automatizados

- Testes unitários para regras de cálculo.
- Testes de integração para fluxo de serviços.
- Execução automática via GitHub Actions.

### 🧮 Regras de Negócio

O sistema implementa uma tabela de decisão financeira rigorosa:

| Modalidade         | Condição           | Regra Aplicada                      |
| ------------------ | ------------------ | ----------------------------------- |
| À vista (Dinheiro) | Pagamento imediato | Desconto de 10%                     |
| À vista (Cartão)   | Pagamento imediato | Desconto de 5%                      |
| Parcelado Curto    | 2x até 6x          | 0% de Juros (Preço original)        |
| Parcelado Longo    | 12x até 24x        | Acréscimo fixo de 10% sobre o total |

**⚠️ Nota:** Tentativas de parcelamento fora dos intervalos permitidos (ex: 7x a 11x) resultam em uma exceção de domínio (Validation Error).

## 🛣️ Como Executar o Projeto

Pré-requisitos: Python 3.12+

### 1. Clonar o repositório:

```bash
git clone https://github.com/argenis972/Loja_app.git
cd Loja_app
```

### 2. Configurar o ambiente virtual (Recomendado)

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

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

Para interagir com o menu visual no terminal:

```bash
python main.py
```
### 6. Executar a API REST (FastAPI)

Para subir o servidor de desenvolvimento:

```bash
uvicorn api.main:app --reload
```

Acesse a documentação automática:
- **Swagger UI**: http://127.0.0.1:8000/docs

### 7. Executar os testes automatizados

```bash
pytest
```

Status atual:

- ✅ 100% dos testes passando

### 📡 Exemplo de Uso da API

**Endpoint**: POST /pagamentos

**Cenário:** Cliente deseja parcelar uma compra de R$ 100,00 em 6 vezes (Sem juros).

**Request Body:**
```json
{
  "opcao": 3,
  "valor": 100.00,
  "num_parcelas": 6
}
```

**Response Body:**
```json
{
  "total": 100.00,
  "valor_parcela": 16.67,
  "num_parcelas": 6,
  "taxas": "0% (Sem juros)",
  "status": "aprovado"
}
```

## 🗺️ **Roadmap de Evolução**

- ✅ 100% dos testes passando

## 🗺️ **Roadmap de Evolução**

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

- LinkedIn: https://www.linkedin.com/in/argenis972/
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

## 📜 Licença

MIT — Sinta-se livre para estudar, adaptar e evoluir.
