from backend.controllers.base_controller import BaseController
from backend.dao.product_dao import ProductDao


class ProductController(BaseController):
    def __init__(self):
        super().__init__(ProductDao())
