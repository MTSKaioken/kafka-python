import os

import uvicorn
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


@app.get('/api/v1/produtos')
async def get_all_products():
    product_service = ProductService()
    products = product_service.get_all_products()
    return {'mensagem': products}


@app.get('/api/v1/produtos/{product_sku}')
async def get_product(product_sku: str):
    product_service = ProductService()
    product = product_service.get_product_by_sku(product_sku)
    return {'mensagem': product}


@app.delete('/api/v1/produtos/{product_sku}')
async def delete_product(product_sku: str):
    product_service = ProductService()
    try:
        status_delete = product_service.delete_product_by_sku(product_sku)
        return {'mensagem': status_delete}
    except Exception as e:
        return {'mensagem': str(e)}


@app.post('/api/v1/produtos')
async def create_product(produto: ProductDTO):
    product_service = ProductService()
    product_service.create_product(produto)
    return {'mensagem': produto}


@app.put('/api/v1/produtos/{product_sku}')
async def update_product(product_sku: str, produto: ProductDTO):
    product_service = ProductService()
    try:
        status_update = product_service.update_product_by_sku(product_sku, produto)
        return {'mensagem': status_update}
    except Exception as e:
        return {'mensagem': str(e)}


# @app.patch('/api/v1/produtos/{product_sku}')
# async def patch_update_product(product_sku: str, produto: ProductDTO):
#     product_service = ProductService()
#     try:
#         status_update = product_service.update_product_by_sku(product_sku, produto)
#         return {'mensagem': status_update}
#     except Exception as e:
#         return {'mensagem': str(e)}


URL_HOST_PROJECT = os.getenv('URL_HOST_PROJECT')
URL_PORT_PROJECT = os.getenv('URL_PORT_PROJECT')
uvicorn.run(app, host=URL_HOST_PROJECT, port=int(URL_PORT_PROJECT))

# @app.patch('/api/produtos/{product_sku}')
# async def update_partial_product(product_sku: str):
#     product_service = ProductService()
#     try:
#         status_delete = product_service.delete_product_by_sku(product_sku)
#         return {'mensagem': status_delete}
#     except Exception as e:
#         return {'mensagem': str(e)}
