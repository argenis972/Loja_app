# 🛍️ Loja App — De Script CLI a API REST em Python

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-009688?style=flat&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testes%20Automatizados-brightgreen?style=flat)
![Status](https://img.shields.io/badge/Status-Em%20Evolu%C3%A7%C3%A3o-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Visão Geral

O **Loja App** é um **laboratório de engenharia de software backend em Python** que documenta, de forma prática, a evolução de um projeto real:  
de um **script CLI funcional** para uma **aplicação backend estruturada**, com **API REST**, **testes automatizados** e **arquitetura em camadas**.

Mais do que “fazer funcionar”, o foco do projeto está em:
- qualidade de código
- clareza de regras de negócio
- separação de responsabilidades
- testabilidade
- evolução incremental consciente

Este não é um sistema comercial pronto, mas um **ambiente controlado de aprendizado técnico**, inspirado em práticas profissionais de backend.

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
## ⚙️ Destaques Técnicos Atuais

### 🚀 FastAPI

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

### 🧮 Regras de Negócio (Pagamentos e Recibos)

O sistema implementa regras financeiras realistas, como:
- Pagamento à vista em dinheiro com 10% de desconto
- Pagamento parcelado de 2x até 24x
- Aplicação de juros progressivos
- Geração automática de recibo contendo:
- - valor total
- - número de parcelas
- - valor de cada parcela
- - descrição da regra aplicada
- - data e hora da transação
Essas regras vivem no domínio, totalmente desacopladas da API ou da UI.

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
