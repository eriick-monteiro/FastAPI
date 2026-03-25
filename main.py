from fastapi import FastAPI
from models import Venda

# Criando a instância da API
app = FastAPI()

# Vendas | Database Hardcoded
vendas = {
    1: {"item": "Refrigerante", "preco_unitario": 4.99, "quantidade": 5},
    2: {"item": "Banco  Madeira", "preco_unitario": 30, "quantidade": 12},
    3: {"item": "Mouse", "preco_unitario": 120, "quantidade": 7},
    4: {"item": "Jogo de Pratos", "preco_unitario": 49.90, "quantidade": 2},
}


# Retorna todas as vendas
@app.get("/")
def home():
    return vendas


# Retorna uma venda específica
@app.get("/venda/{id_venda}")
def retorna_venda(id_venda:int):
    """"""

    # Verificando se o id existe
    if id_venda in vendas:

        # Retornando a venda
        return vendas[id_venda]
    else:
        return {"Erro": "ID da Venda inexistetnte"}


# Retorna uma venda específica
@app.post("/venda")
def adiciona_venda(venda: Venda):
    """"""

    item_novo = {
        "item": venda.item,
        "preco_unitario": venda.preco_unitario,
        "quantidade": venda.quantidade
    }

    # Calculando o próximo ID com base nas chaves já existentes
    proximo_id = max(vendas.keys()) + 1

    # Adicionando item novo ao dicionario
    vendas[proximo_id] = item_novo

    # Retornando item adicionado
    return vendas[proximo_id]


# Edita uma venda específica
@app.put("/venda/{id_venda}")
def atualiza_venda(id_venda:int, venda: Venda):
    """"""

    # Verificando se o id existe
    if id_venda in vendas:

        # Nosso novo item
        novo_item = {
            "item": venda.item,
            "preco_unitario": venda.preco_unitario,
            "quantidade": venda.quantidade
        }

        # Substituindo o item antigo pelo novo
        vendas[id_venda] = novo_item

        # Retornando item atualizado
        return vendas[id_venda]
    else:
        return {"Erro": "ID da Venda inexistetnte"}


# Deleta uma venda específica
@app.delete("/venda/{id_venda}")
def deleta_venda(id_venda:int):
    """"""

    # Verificando se o id existe
    if id_venda in vendas:

        # Deletando do banco de fato
        del vendas[id_venda]

        # Retornando sucesso da deleção
        return {"Sucesso": "Item deletado"}
    else:
        return {"Erro": "ID da Venda inexistetnte"}

