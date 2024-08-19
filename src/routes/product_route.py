from fastapi import APIRouter
from src.services.product_service import ProductService
from src.dtos.product_dto import ProductDTO
router = APIRouter(prefix='/api/v1')


@router.get('/produtos')
async def get_all_products():
    product_service = ProductService()
    products = product_service.get_all_products()
    return {'mensagem': products}


@router.get('/produtos/{product_sku}')
async def get_product(product_sku: str):
    product_service = ProductService()
    product = product_service.get_product_by_sku(product_sku)
    return {'mensagem': product}


@router.delete('/produtos/{product_sku}')
async def delete_product(product_sku: str):
    product_service = ProductService()
    try:
        status_delete = product_service.delete_product_by_sku(product_sku)
        return {'mensagem': status_delete}
    except Exception as e:
        return {'mensagem': str(e)}


@router.post('/produtos')
async def create_product(produto: ProductDTO):
    product_service = ProductService()
    product_service.create_product(produto)
    return {'mensagem': produto}


@router.put('/produtos/{product_sku}')
async def update_product(product_sku: str, produto: ProductDTO):
    product_service = ProductService()
    try:
        status_update = product_service.update_product_by_sku(product_sku, produto)
        return {'mensagem': status_update}
    except Exception as e:
        return {'mensagem': str(e)}

