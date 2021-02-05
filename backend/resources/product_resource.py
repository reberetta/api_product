from flask_restful import fields, marshal_with

from backend.dao.product_dao import ProductDao
from backend.models.product import Product
from backend.resources.base_resource import BaseResource


class ProductResource(BaseResource):
    fields = {
        'id_': fields.Integer,
        'name': fields.String,
        'description': fields.String,
        'price': fields.Float
    }

    def __init__(self):
        self.__dao = ProductDao()
        self.__model_type = Product
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)
