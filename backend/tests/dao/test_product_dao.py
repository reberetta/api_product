import sys
sys.path.append('.')

from backend.dao.product_dao import ProductDao
from backend.models.product import Product
import pytest


class TestProductDao:
    @pytest.fixture
    def create_product(self):
        return Product('Product Test', 'Testing Product', 50.0)

    @pytest.fixture
    def create_product_dao(self):
        return ProductDao()

    def test_product_dao_instance(self, create_product_dao):
        product_dao = create_product_dao
        assert isinstance(product_dao, ProductDao)

    def test_product_create(self, create_product, create_product_dao):
        product = create_product_dao.save(create_product)
        assert product.id_ is not None
        create_product_dao.delete(product)

    def test_product_read_by_id(self, create_product, create_product_dao):
        product = create_product_dao.save(create_product)
        product_read = create_product_dao.read_by_id(product.id_)
        assert isinstance(product_read, Product)
        assert product.name == product_read.name
        assert product.description == product_read.description
        assert product.price == product_read.price
        create_product_dao.delete(product_read)

    def test_product_read_all(self, create_product_dao):
        products = create_product_dao.read_all()
        assert isinstance(products, list)
        assert all(isinstance(product, Product) for product in products)

    def test_product_delete(self, create_product, create_product_dao):
        product_save = create_product_dao.save(create_product)
        product = create_product_dao.read_by_id(product_save.id_)
        create_product_dao.delete(product)
        product_read = create_product_dao.read_by_id(product_save.id_)
        assert product_read is None
