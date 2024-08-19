from src.dao.product_dao import ProductDao
from src.dtos.product_dto import ProductDTO


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
        if product:
            # todo estudar o **
            dto = ProductDTO(**product)
            return dto
        else:
            return None

    def delete_product_by_sku(self, sku: str):
        found = self.get_product_by_sku(sku)
        try:
            if found:
                self.product_dao.delete_product_by_sku(sku)
                return 'deletado com sucesso!'
            else:
                return f'SKU {sku} não encontrado!'
        except Exception as e:
            print(e)
            raise RuntimeError(f'erro ao deletar produto de SKU {sku}!')

    def update_product_by_sku(self, sku: str, dto: ProductDTO):
        found = self.get_product_by_sku(sku)
        if found:
            dto.sku = sku
            model = dto.to_model()
            self.product_dao.update_product_by_sku(sku, model)
            return f'{sku} atualizado com sucesso!'
        else:
            return f'SKU {sku} não encontrado!'


