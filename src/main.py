import os
from typing import Dict

from dotenv import load_dotenv
from fastapi import FastAPI
from src.services.product_service import ProductService
from src.dtos.product_dto import ProductDTO


def load_environment():
    if os.path.isfile('.env'):
        load_dotenv('.env')
    elif os.path.isfile('.env.dev'):
        load_dotenv('.env.dev')
    else:
        raise RuntimeError("Defina as variaveis do projeto no .env")


load_environment()
app = FastAPI()

produtos: Dict[int, ProductDTO] = {
    1: ProductDTO(sku="001", description="Camiseta Básica", quantity=100, price=29.99),
    2: ProductDTO(sku="002", description="Calça Jeans", quantity=50, price=79.99),
    3: ProductDTO(sku="003", description="Tênis Esportivo", quantity=30, price=119.99),
    4: ProductDTO(sku="004", description="Jaqueta de Couro", quantity=20, price=199.99),
    5: ProductDTO(sku="005", description="Óculos de Sol", quantity=75, price=49.99),
}

@app.get('/api/produtos')
async def getProdutos():
    product_service = ProductService()
    products = product_service.get_all_products()
    return {'mensagem': products}


@app.get('/api/produtos/{product_sku}')
async def getProduto(product_sku: str):
    product_service = ProductService()
    product = product_service.get_product_by_sku(product_sku)
    return {'mensagem': product}


@app.delete('/api/produtos/{product_sku}')
async def deleteProduto(product_sku: str):
    product_service = ProductService()
    try:
        status_delete = product_service.delete_product_by_sku(product_sku)
        return {'mensagem': status_delete}
    except Exception as e:
        return {'mensagem': str(e)}




@app.post('/api/produtos')
async def postProduto(produto: ProductDTO):
    product_service = ProductService()
    product_service.create_product(produto)
    return {'mensagem': produto}
