# 🛍️ Loja App — Evolução de Script CLI para Backend em Python

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?style=flat&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testes%20Automatizados-brightgreen?style=flat)
![Status](https://img.shields.io/badge/Status-Estável-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Visão Geral

**Loja App** é um **laboratório de engenharia de software backend em Python**, focado na modelagem e evolução de **regras de negócio financeiras**, especialmente no cálculo de **pagamentos parcelados** e geração de **recibos**.

O objetivo do projeto não é entregar um sistema comercial final, mas **documentar decisões técnicas reais**, priorizando:

- Clareza das regras de negócio  
- Separação de responsabilidades (Clean Architecture)  
- Testabilidade  
- Evolução incremental  
- Qualidade de código
# 
---

## 🧠 Evolução do Projeto

1. Implementação inicial de cálculos simples via CLI  
2. Introdução de regras de parcelamento e descontos  
3. Refatoração para arquitetura em camadas  
4. **Atualização Profissional (v2):** regras de mercado (parcelamento sem juros) e interface CLI refinada  

---

## 🧱 Arquitetura do Projeto

Arquitetura modular inspirada em **Clean Architecture / Hexagonal**, mantendo dependências sempre apontando para dentro (domínio).

```text
Loja_app/
├── api/                 # 🌐 Camada de API (FastAPI)
│   ├── main.py
│   ├── pagamentos_api.py
│   └── dtos/            # Contratos de entrada/saída
│
├── config/              # ⚙️ Configurações e taxas externas
|   ├── settings.py              
│   └── taxas.json       
│
├── domain/              # 🧠 Regras de negócio puras
│   ├── exceptions.py
│   ├── recibo.py        # Entidade Recibo
│   └── calculadora.py   # Core de cálculo financeiro
│
├── services/            # ⚙️ Casos de uso / orquestração
│   ├── pagamento_service.py
│   └── recibo_repository.py
│
├── infrastructure/      # 💾 Implementações técnicas
│   └── storage.py       # Persistência de arquivos
│
├── receipts/            # 📄 Esta pasta é ignorada pelo Git (.gitignore)
│   └── *.json / *.txt   # Todos os arquivos gerados (JSON, TXT) são temporários e não devem ser versionados.
│
├── tests/               # 🧪 Testes automatizados (Pytest)
│   ├── test_calculadora.py
│   ├── test_recibo.py
│   └── ...
│
├── ui/                  # 🖥️ Interface CLI
│   ├── menu.py
│   └── validacoes.py
│
├── .gitignore
├── main_api.py   
├── main.py              # Entry point CLI
├── README.md             
└── requirements.txt

```
## 🚀 Destaques Técnicos

### API REST (FastAPI)

- Endpoints para pagamentos, recibos e consultas
- Documentação automática via Swagger: http://127.0.0.1:8000/docs

### CLI Profissional

- Design visual com caracteres box-drawing (╔═╗)
- Formatação de valores monetários e texto alinhado
- Validações robustas de inputs

### Testes Automatizados

- Cobertura das regras de negócio, serviços e persistência
- Pytest garante segurança para refatorações

### 🧮 Regras de Negócio

| Modalidade         | Condição           | Regra Aplicada                      |
| ------------------ | ------------------ | ----------------------------------- |
| À vista (Dinheiro) | Pagamento imediato | Desconto de 10%                     |
| À vista (Cartão)   | Pagamento imediato | Desconto de 5%                      |
| Parcelado Curto    | 2x até 6x          | 0% de Juros (Preço original)        |
| Parcelado Longo    | 12x até 24x        | Acréscimo fixo de 10% sobre o total |

Tentativas de parcelamento fora dos intervalos definidos resultam em uma exceção de validação (Domain Exception).

## 🛣️ Como Executar o Projeto

### 1. Clonar o repositório:
```bash
git clone https://github.com/argenis972/Loja_app.git
cd Loja_app
```

### 2. Executar via CLI as dependencias:

```bash
pip install -r requirements.txt
```

### 3. Executar via CLI:

```bash
python main.py
```
### 4. Executar a API REST (FastAPI)

```bash
uvicorn api.main:app --reload
```
Acesse:
- Swagger: http://127.0.0.1:8000/docs

### 5. Executar os testes automatizados

```bash
pytest
```
Status atual:

- ✅ 100% dos testes passando

## 🗺️ Roadmap de Evolução

| Feature                                   | Status          |
| ----------------------------------------- | --------------- |
| Testes automatizados com pytest           | ✅ Concluído     |
| API REST com FastAPI                      | ✅ Concluído     |
| Configuração externa (taxas)              | ✅ Concluído     |
| Exportação de recibos em PDF              | 🟡 Em progresso |
| Persistência em banco (SQLite/PostgreSQL) | 🟡 Em progresso |


## 🧠 Filosofia do Projeto

- Clareza sobre complexidade desnecessária
- Boas práticas de design de software
- Decisões conscientes baseadas em requisitos

## 👤 Autor 

**Argenis López** <br />
*Backend Developer em formação contínua, com foco em Python, arquitetura de software e qualidade de código.*

## 📬 Contato

- LinkedIn: https://www.linkedin.com/in/argenis972/
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

## 📜 Licença

MIT — Sinta-se livre para estudar, adaptar e evoluir.
