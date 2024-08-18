from pydantic import BaseModel
from src.models.product import Product


class ProductDTO(BaseModel):
    sku: str
    description: str
    quantity: int
    price: float

    def to_model(self):
        model = Product()
        model.sku = self.sku
        model.description = self.description
        model.quantity = self.quantity
        model.price = self.price
        return model

    def to_dto(self, model: dict):
        self.sku = self.sku
        self.description = self.description
        self.quantity = self.quantity
        self.price = self.price
        return self
