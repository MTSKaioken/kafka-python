from src.dao.product_dao import ProductDao
from src.dtos.product_dto import ProductDTO
import json

class ProductService:

    def __init__(self):
        self.product_dao = ProductDao()

    def create_product(self, dto: ProductDTO):
        model = dto.to_model()
        self.product_dao.add_product(model)
    def get_all_products(self):
        products = self.product_dao.get_all_products()
        list = []
        for product in products:
            dto = ProductDTO(**product)
            list.append(dto)
        return list

    def get_product_by_sku(self, sku: str):
        product = self.product_dao.get_product_by_sku(sku)
        # todo estudar o **
        dto = ProductDTO(**product)
        return dto

