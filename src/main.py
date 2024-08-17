from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


class Produto(BaseModel):
    sku: str
    descricao: str
    quantidade: int
    preco: float


produtos: Dict[int, Produto] = {
    1: Produto(sku="001", descricao="Camiseta Básica", quantidade=100, preco=29.99, custo=15.00),
    2: Produto(sku="002", descricao="Calça Jeans", quantidade=50, preco=79.99, custo=40.00),
    3: Produto(sku="003", descricao="Tênis Esportivo", quantidade=30, preco=119.99, custo=60.00),
    4: Produto(sku="004", descricao="Jaqueta de Couro", quantidade=20, preco=199.99, custo=100.00),
    5: Produto(sku="005", descricao="Óculos de Sol", quantidade=75, preco=49.99, custo=25.00),
}

@app.get('/api/produtos')
async def getProdutos():
    return {'mensagem': produtos}

@app.get('/api/produtos/{product_id}')
async def getProduto(product_id: int):
    return {'mensagem': produtos.get(product_id)}

@app.delete('/api/produtos/{product_id}')
async def deleteProduto(product_id: int):
    produtos.__delitem__(product_id)
    return {'mensagem': produtos}

@app.post('/api/produtos')
async def postProduto(produto: Produto) -> object:
    produtos[produtos.__len__() + 1] = produto
    return {'mensagem': produtos}
