# 🛍️ Loja App — Evolução de Script CLI para Backend em Python

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?style=flat&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testes%20Automatizados-brightgreen?style=flat)
![Status](https://img.shields.io/badge/Status-Em%20Evolu%C3%A7%C3%A3o-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Visão Geral

O **Loja App** é um **laboratório de engenharia de software backend em Python**, focado na modelagem e evolução de **regras de negócio financeiras**, especialmente no cálculo de **pagamentos parcelados e geração de recibos**.

Este repositório representa a **versão consolidada do projeto**, após ciclos de experimentação, refatoração e ajustes conscientes nas regras de cálculo.  
O objetivo não é entregar um sistema comercial final, mas **documentar decisões técnicas reais**, priorizando:

- clareza das regras de negócio
- separação de responsabilidades
- testabilidade
- evolução incremental
- qualidade de código

O projeto começou como um ambiente de experimentação e foi estabilizado nesta versão para servir como **base principal do repositório**.

## 🧠 Evolução do Projeto

O desenvolvimento do Loja App seguiu uma abordagem incremental:

1. Implementação inicial de cálculos simples via CLI
2. Introdução de regras de parcelamento e descontos
3. Ajustes na geração de recibos para refletir corretamente:
   - valor total
   - número de parcelas
   - valor individual de cada parcela
4. Refatoração para melhorar legibilidade, testes e isolamento das regras de negócio

A lógica atual de recibos parcelados é resultado desse processo de exploração e consolidação, e representa a base estável do projeto.

---

## 🧠 Narrativa de Evolução Técnica

O projeto iniciou como um **script de terminal (CLI)** para simular pagamentos simples.  
Com o tempo, foi refatorado para refletir decisões reais de engenharia:

- Extração de **regras de negócio puras** para o domínio
- Introdução de uma camada de **serviços (casos de uso)**
- Isolamento da **persistência** em infraestrutura
- Criação de uma **API REST com FastAPI**
- Implementação de **testes automatizados com Pytest**
- Padronização de contratos via **DTOs**
- Garantia de regras financeiras reais (parcelamento, juros, descontos)

Essa evolução é intencional e documentada no código.

---

## 🧱 Arquitetura do Projeto

O projeto segue uma arquitetura modular inspirada em **Clean Architecture / Hexagonal**, mantendo dependências sempre apontando para dentro (domínio).

```text
Loja_app/
├── api/                         # 🌐 Camada de API (FastAPI)
│   ├── main.py
│   ├── pagamentos_api.py        # Endpoints HTTP
│   └── dtos/                    # Contratos de entrada/saída
│       ├── __init__.py
│       ├── pagamento_request.py
│       └── pagamento_response.py
│
├── data/
│   └── recibos.txt
│
├── domain/                      # 🧠 Regras de negócio puras
│   ├── exceptions.py
│   ├── __init__.py 
│   ├── recibo.py                # Entidade Recibo
│   └── calculadora.py           # Cálculo de valores, juros e descontos
│
├── services/                    # ⚙️ Casos de uso / Orquestração
│   ├── __init__.py             
│   ├── pagamento_service.py
│   └── recibo_repository.py
│   
├── infrastructure/              # 💾 Implementações técnicas
│   ├── __init__.py           
│   └── storage.py               # Persistência em arquivo
│
├── tests/                       # 🧪 Testes automatizados (Pytest)
│   ├── __init__.py                       
│   ├── test_calculadora.py
│   ├── test_recibo.py
│   ├── test_storage.py
│   ├── test_pagamento_service.py
│   └── test_api_pagamentos.py
│
├── ui/                          # 🖥️ Interface CLI
│   ├── __init__.py
│   ├── menu.py
│   └── validacoes.py
│
├── .gitignore
├── main.py                      # Interface CLI
├── main_api.py                  # Entry point da API FastAPI
└── README.md
```
## 🧩 Decisões de Design

- **Separação por camadas (domain / services / infrastructure / ui)**  
  Para isolar regras de negócio e permitir evolução sem reescrita do núcleo.

- **Domínio independente de interface**  
  A lógica de cálculo e geração de recibos não depende da CLI.

- **Persistência simples em arquivo**  
  Escolhida intencionalmente para manter foco nas regras de negócio e facilitar inspeção manual durante o desenvolvimento.
  A camada está isolada para futura migração para banco de dados.

Essas decisões priorizam clareza e testabilidade, mesmo com maior complexidade inicial.

## ⚙️ Destaques Técnicos Atuais

### 🚀 FastAPI

A API REST representa a etapa atual de exposição dos fluxos de negócio, mantendo o projeto aberto a evoluções.

- Exposição dos fluxos de pagamento via API REST
- Documentação automática com Swagger e Redoc
- Separação clara entre API, domínio e serviços <br>
Acesso à documentação:
```bash
http://127.0.0.1:8000/docs
```
### 🧪 Pytest

- Cobertura completa das regras de negócio
- Testes para:
- - domínio (cálculos e recibos)
- - serviços
- - persistência
- - API
- Segurança para refatorações futuras

## 🧮 Regras de Negócio

O sistema implementa regras financeiras explícitas e testáveis, incluindo:

- Pagamento à vista com desconto
- Pagamento parcelado em múltiplas parcelas
- Cálculo automático:
  - do valor total
  - do valor de cada parcela
  - da descrição da regra aplicada
- Geração de recibo contendo:
  - valores detalhados
  - número de parcelas
  - data e hora da transação

Essas regras residem no domínio e não dependem da interface (CLI) ou de mecanismos de persistência.

## 🚀 Como Executar o Projeto
### 1. Clonar o repositório:
```bash
git clone https://github.com/argenis972/Loja_app.git
```

2. Acesse o diretório:

```bash
cd Loja_app
```
### 2️⃣ Executar a API REST (FastAPI)
```bash
uvicorn main_api:app --reload
```
Acesse:
- Swagger: http://127.0.0.1:8000/docs

### 3️⃣ Executar a aplicação via CLI

```bash
python main.py
```
### 4️⃣ Executar os testes automatizados

```bash
pytest
```
Status atual:

- ✅ 100% dos testes passando

## 🔧 🛣️ Roadmap de Evolução

- ✅ Testes automatizados com pytest (concluído)
Cobertura completa das regras de negócio, serviços e persistência.
- ✅ API REST com FastAPI (concluído)
Exposição dos fluxos de pagamento via endpoints HTTP.
- 🟡 Configuração externa
Mover taxas (% juros e descontos) para arquivos .env ou .json.
- 🟡 Exportação de recibos
Gerar recibos em PDF.
- 🟡 Persistência em banco de dados
Migrar do arquivo .txt para SQLite ou outro banco relacional.

## 🧠 Filosofia do Projeto
Este repositório não busca “atalhos”.
Ele prioriza:
- clareza
- boas práticas
- decisões conscientes
- aprendizado sólido
Cada refatoração é respaldada por testes.

## 👤 Autor 

**Argenis López** <br />
*Backend Developer em formação contínua, com foco em Python, arquitetura de software e qualidade de código.*

## 📬 Contato

- LinkedIn: https://www.linkedin.com/in/argenis-lópez-649701304
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

## 📜 Licença

Este projeto está sob a licença MIT. <br>
Sinta-se livre para estudar, adaptar e evoluir.
