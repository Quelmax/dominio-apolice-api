# 📄 Apolice API

API para gerenciamento de apólices de seguro, construída com **FastAPI** e organizada segundo princípios de **Domain-Driven Design (DDD)**.

---

## 📦 Tecnologias utilizadas

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) – servidor ASGI
- [UUID](https://docs.python.org/3/library/uuid.html) – identificadores únicos para entidades
- [Poetry](https://python-poetry.org/) *(opcional)* para gerenciamento de dependências

---

## 📁 Estrutura do Projeto

apolice-api/
│
├── app/  ← 🧠 Núcleo da aplicação
│   ├── domain/                ← 📘 Regras de negócio (entidades + valores)
│   │   ├── cpf.py             ← Validando e representando CPF
│   │   └── apolice.py         ← Entidade Apólice com datas e prêmio
│   │
│   ├── services/              ← ⚙️ Casos de uso do sistema
│   │   └── servico_criar_apolice.py  ← Lógica para criar uma nova apólice
│   │
│   ├── repositories/          ← 💾 Acesso a dados
│   │   └── apolice_repository_memoria.py ← Repositório em memória (mock)
│   │
│   ├── api/                   ← 🌐 Interface HTTP (FastAPI)
│   │   └── routes_apolices.py ← Rota POST /apolices
│   │
│   └── main.py                ← 🚀 Ponto de entrada da aplicação
│
├── tests/  ← 🧪 Testes automatizados
│   └── test_criar_apolice.py
│
├── requirements.txt  ← 📦 Dependências do projeto
└── README.md         ← 📝 Manual do projeto
