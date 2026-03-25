from pydantic import BaseModel

class Venda(BaseModel):
    item: str
    preco_unitario: float
    quantidade: int