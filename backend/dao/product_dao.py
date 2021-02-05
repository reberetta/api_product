from backend.dao.base_dao import BaseDao
from backend.models.product import Product


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)
