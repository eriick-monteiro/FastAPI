# API de Vendas com FastAPI

API REST para gerenciamento de vendas construída com FastAPI.

## 🛠️  Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-4051B5?style=for-the-badge&logo=gunicorn&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

## 📦 Instalação

```bash
pip install -r requirements.txt
```

## ▶️ Executando

```bash
uvicorn main:app --reload
```

A API ficará disponível em `http://localhost:8000`.

Documentação interativa:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📡 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Lista todas as vendas |
| GET | `/venda/{id}` | Retorna uma venda pelo ID |
| POST | `/venda` | Cria uma nova venda |
| PUT | `/venda/{id}` | Atualiza uma venda pelo ID |
| DELETE | `/venda/{id}` | Remove uma venda pelo ID |

## 🗂️ Modelo de Dados

```json
{
  "item": "string",
  "preco_unitario": 0.0,
  "quantidade": 0
}
```

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `item` | string | Nome do produto |
| `preco_unitario` | float | Preço unitário |
| `quantidade` | int | Quantidade vendida |

## 🚀 Exemplo de Uso

**Criar uma venda:**
```bash
curl -X POST http://localhost:8000/venda \
  -H "Content-Type: application/json" \
  -d '{"item": "Notebook", "preco_unitario": 2500.00, "quantidade": 1}'
```

**Listar todas as vendas:**
```bash
curl http://localhost:8000/
```

## 📂 Estrutura do Projeto

```bash
📦 FastAPI/
├── 📂 models/
│   ├── 📄 __init__.py
│   └── 📊 venda.py     # Modelo de dados Venda
├── 🐍 main.py          # Aplicação principal e endpoints
├── 🙈 .gitignore
├── 📖 README.md
└── 📦 requirements.txt    # Dependências

```

> **Nota:** Os dados são armazenados em memória e são resetados ao reiniciar o servidor.
