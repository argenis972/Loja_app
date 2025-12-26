# 🧾 Loja App (Python)

Aplicação de console em Python que simula um **sistema simples de pagamentos de uma loja**, com cálculo de descontos, parcelamentos e geração de recibos.

O objetivo do projeto é praticar **organização de código**, separação de responsabilidades e uma arquitetura simples inspirada em boas práticas de backend.

Não é um sistema comercial real. É um projeto educacional em evolução.

---

## 📌 Funcionalidades

- Pagamento à vista em dinheiro (10% de desconto)
- Pagamento à vista em cartão (5% de desconto)
- Pagamento parcelado:
  - 2x sem juros
  - 3x até 24x com juros fixos
- Validação de dados de entrada
- Geração de recibo estruturado
- Salvamento do recibo em arquivo de texto
- Interface via terminal (CLI)

---

## 🗂 Estrutura Atual do Projeto

```text
Loja_app/
│
├── Calculadora_de_pagamentos.py   # Arquivo principal da aplicação
├── README.md
├── .gitignore
│
└── data/
    └── recibos.txt                # Arquivo de saída dos recibos
```
  
A estrutura atual do projeto é simples, com todos os componentes principais consolidados em um único arquivo para facilitar a compreensão inicial.




## 🗂 Estrutura Futura Planejada


A estrutura futura planejada visa separar as responsabilidades em módulos distintos, facilitando a manutenção e escalabilidade do código. A seguir está a estrutura proposta:


```text
loja_app/
│
├── main.py                 # Ponto de entrada
│
├── domain/
│   ├── __init__.py
│   ├── recibo.py           # Dataclass Recibo
│   └── calculadora.py      # Regras de negócio
│
├── services/
│   ├── __init__.py
│   └── pagamento_service.py # Fluxo principal
│
├── ui/
│   ├── __init__.py
│   ├── menu.py              # Prints e inputs
│   └── validacoes.py        # Validação de dados
│
├── infrastructure/
│   ├── __init__.py
│   └── storage.py           # Salvar e ler arquivos
│
└── data/
    └── recibos.txt
```
---
Essa refatoração tem como objetivo melhorar a legibilidade, manutenção e escalabilidade do código.

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- dataclasses
- Programação orientada a objetos
- Estrutura modular (em evolução)
- Entrada e saída via console

## 🚀 Como Executar o Projeto
- Clonar o repositório:
```bash
git clone https://github.com/argenis972/Loja_app.git
```

Entrar no diretório do projeto:

```bash
cd Loja_app
```
Executar a aplicação (estrutura atual):
```bash
python Calculadora_de_pagamentos.py
```
Seguir as instruções exibidas no terminal.

## 📄 Saída

- O recibo é exibido no terminal
- Uma cópia é salva em:
```
data/recibos.txt
```

Cada execução adiciona um novo recibo com data e hora.

## 🎯 Objetivo do Projeto

- Praticar lógica de negócio
- Aprender a estruturar projetos Python
- Evoluir de script único para arquitetura modular
- Aplicar boas práticas de backend em projetos pequenos

## 🔧 Possíveis Melhorias Futuras

- Concluir a refatoração modular
- Exportar recibos em PDF
- Configuração externa de taxas e descontos
- Testes automatizados
- Persistência em banco de dados
- Interface gráfica ou aplicação web

## 👤 Autor 

**Argenis López** <br />
*Projeto pessoal com fins educacionais e de aprendizado em backend Python.*

## 📜 Licença

Uso livre para fins educacionais e pessoais.

## 📬 Contato

- LinkedIn: https://www.linkedin.com/in/argenis-lópez-649701304
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972