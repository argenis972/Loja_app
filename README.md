# 🛍️ Loja App — Calculadora de Pagamentos em Python

![CI](https://github.com/argenis972/Loja_app/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?style=flat&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testes%20Automatizados-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Visão Geral

**Loja App** é um projeto backend em **Python** para **cálculo de pagamentos parcelados**, com foco em regras de negócio financeiras reutilizáveis entre **CLI** e **API REST**.

Principais pontos:

- **Regras de negócio desacopladas** (camada `domain`).
- **Arquitetura em camadas** (domain / services / infra).
- **API REST** com FastAPI.
- **Testes automatizados** com pytest e pipeline de CI.

---

## 🧱 Estrutura do Projeto (atual)

```text
Loja_app/
├── .github/
│   └── workflows/
│       └── tests.yml
├── api/
├── config/
├── domain/
├── infra/
├── infrastructure/
├── services/
├── tests/
├── ui/
├── .flake8
├── .gitignore
├── .pre-commit-config.yaml
├── app.log
├── main.py
├── main_api.py
├── README.md
└── requirements.txt
```

> Observação: a listagem acima reflete a estrutura presente na branch **main**.

---

## 🧮 Regras de Negócio (resumo)

| Modalidade         | Condição           | Regra Aplicada                      |
| ------------------ | ------------------ | ----------------------------------- |
| À vista (Dinheiro) | Pagamento imediato | Desconto de 10%                     |
| À vista (Cartão)   | Pagamento imediato | Desconto de 5%                      |
| Parcelado Curto    | 2x até 6x          | 0% de Juros (Preço original)        |
| Parcelado Longo    | 12x até 24x        | Acréscimo fixo de 10% sobre o total |

**Nota:** Parcelamentos fora dos intervalos permitidos (ex: 7x a 11x) devem gerar erro/validação no domínio.

---

## 🛠️ Como Executar

Pré-requisitos: **Python 3.12+**

### 1) Clonar

```bash
git clone https://github.com/argenis972/Loja_app.git
cd Loja_app
```

### 2) Ambiente virtual

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3) Instalar dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executar via CLI

```bash
python main.py
```

---

## 🌐 Executar API REST

Há dois entrypoints no repositório:

- `api.main:app` (módulo dentro da pasta `api/`)
- `main_api.py` (arquivo na raiz)

Use o que fizer sentido para seu ambiente.

### Opção A (recomendado):

```bash
uvicorn api.main:app --reload
```

### Opção B:

```bash
uvicorn main_api:app --reload
```

Documentação automática:

- Swagger UI: http://127.0.0.1:8000/docs

---

## 🧪 Testes

```bash
pytest
```

---

## 👤 Autor

**Argenis López**

- LinkedIn: https://www.linkedin.com/in/argenis972/
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

---

## 📜 Licença

MIT — Sinta-se livre para estudar, adaptar e evoluir.
