from src.dao.connection_factory import get_connection
from src.models.product import Product


class ProductDao:
    def __init__(self):
        connection = get_connection()
        self.client = connection['products']

    def add_product(self, model: Product):
        self.client.insert_one(model.__dict__)

    def get_all_products(self):
        return self.client.find()

    def get_product_by_sku(self, sku: str):
        return self.client.find_one({'sku': sku})

    def delete_product_by_sku(self, sku: str):
        self.client.delete_one({'sku': sku})

    def update_product_by_sku(self, sku: str, model: Product):
        self.client.update_one({'sku': sku}, {'$set': model.__dict__})
