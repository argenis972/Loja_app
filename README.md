# 🛍️ Loja App (Backend Python)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Aplicação simples desenvolvida em Python com foco em organização de código, regras de negócio claras e evolução progressiva para um backend mais estruturado.

O projeto simula o funcionamento básico de uma loja, permitindo o cadastro de produtos, cálculo de valores, aplicação de taxas e descontos, além da geração de recibos.

---

## 🎯 Objetivo do Projeto

- ✅ Organização e refatoração de código
- ✅ Separação de responsabilidades
- ✅ Validações de regras de negócio
- ✅ Escrita de código limpo e legível
- ✅Evolução gradual de um script simples para uma aplicação estruturada

> *Não é um sistema comercial completo, mas sim um laboratório de aprendizado sólido e incremental.*
---

## 🗂 Estrutura Atual do Projeto 

O projeto segue uma arquitetura modular inspirada em conceitos de Clean Architecture:

```text
loja_app/
│
├── main.py                  #  Ponto de entrada da aplicação
│
├── domain/                  # 🧠 O "Coração" da regra de negócio
│   ├── __init__.py
│   ├── recibo.py            # Modelo de dados (Dataclass)
│   └── calculadora.py       # Lógica pura de cálculos
│
│
├── services/                # ⚙️ Orquestração de fluxos
│   ├── __init__.py
│   └── pagamento_service.py 
│
│
├── ui/                      # 🖥️ Interface com o Usuário (CLI)
│   ├── __init__.py
│   ├── menu.py              # Exibição e Captura de dados
│   └── validacoes.py        # Sanitização de entradas
│
├── infrastructure/          # 💾 Persistência e Dados
│   ├── __init__.py
│   ├── storage.py           # Manipulação de arquivos (Salvar e ler)
│   └── data/
│       ├── .gitkeep
│       └── recibos.txt      # Histórico de recibos gerados
│
└── tests/                   # 🧪 Testes Automatizados (Em construção)
    ├── __init__.py
    ├── test_calculadora.py
    ├── test_recibo.py
    └── test_storage.py
    └── recibos.txt

```
## ⚙️ Funcionalidades Atuais

- Cadastro dinâmico de produtos via terminal.
- Motor de cálculo com aplicação de taxas e descontos.
- Validação robusta (impede preços negativos ou nomes vazios).
- Validações de dados de entrada
- Geração de recibo em formato textual
- Log Automático: Salva uma cópia do recibo em data/recibos.txt com timestamp.

## 🚀 Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos
- Estrutura modular
- Git para versionamento

## 🚀 Como Executar o Projeto
1. Clonar o repositório:
```bash
git clone [https://github.com/argenis972/Loja_app.git](https://github.com/argenis972/Loja_app.git)
```

2. Acesse o diretório:

```bash
cd Loja_app
```
Execute o arquivo principal no Terminal (CMD):
```bash
python main.py
```
(Caso tenha múltiplas versões do Python, tente python3 main.py)

## 📄 Saída

- O recibo é exibido no terminal
- Uma cópia é salva em:
```
data/recibos.txt
```

Cada execução adiciona um novo recibo com data e hora.

## 🔧 Possíveis Melhorias Futuras

- Testes: Finalizar a cobertura de testes unitários com pytest.
- Configuração: Mover taxas (% impostos) para um arquivo de configuração .env ou .json.
- Exportação: Gerar recibos em PDF.
- API: Transformar o backend para uso com FastAPI
- Banco de Dados: Implementar SQLite para persistir produtos e histórico.

## 👤 Autor 

**Argenis López** <br />
*Em desenvolvimento contínuo, com foco em aprendizado, refatoração e consolidação de fundamentos de backend em Python.*

## 📜 Licença

Este projeto está sob a licença MIT - sinta-se livre para usar e modificar para estudos.

## 📬 Contato

- LinkedIn: https://www.linkedin.com/in/argenis-lópez-649701304
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972