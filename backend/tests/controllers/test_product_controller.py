import sys
sys.path.append('.')

import pytest

from backend.controllers.base_controller import BaseController
from backend.controllers.product_controller import ProductController
from backend.models.product import Product


@pytest.fixture
def create_instance():
    product = ProductController()
    return product

def test_product_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, ProductController)

def test_read_all_return_list(create_instance):
    result = create_instance.read_all()
    assert isinstance(result, list)

def test_create_product(create_instance):
    name = "Nome"
    description = "Descricao"
    price = 54.12
    prod = Product(name, description, price)

    result = create_instance.create(prod)

    assert result.id_ is not None
    assert result.name == name
    assert result.description == description
    assert result.price == price

    create_instance.delete(result)

def test_update_product(create_instance):
    name = "Nome"
    description = "Descrição"
    price = 12.92
    prod = Product(name, description, price)
    created = create_instance.create(prod)

    name2 = "Novo"
    description2 = "Outra"
    price2 = 23.48
    created.name = name2
    created.description = description2
    created.price = price2
    result = create_instance.update(created)

    assert result.id_ is not None
    assert result.name == name2
    assert result.description == description2
    assert result.price == price2

    create_instance.delete(result)

def test_delete_product(create_instance):
    name = "Nome"
    description = "Descrição"
    price = 78.98
    prod = Product(name, description, price)
    created = create_instance.create(prod)

    create_instance.delete(created)

    with pytest.raises(Exception) as error:
        create_instance.read_by_id(created.id_)
        assert str(error.value) == 'Object not found in the database.'

def test_read_by_id_return_product(create_instance):
    name = "Nome"
    description = "Descrição"
    price = 782.23
    prod = Product(name, description, price)
    created = create_instance.create(prod)

    result = create_instance.read_by_id(created.id_)

    assert isinstance(result, Product)
    assert result.name == name
    assert result.description == description
    assert result.price == price

    create_instance.delete(created)

def test_read_by_id_invalid_id_exception(create_instance):
    with pytest.raises(Exception) as error:
        create_instance.read_by_id(99999)
    assert str(error.value) == 'Object not found in the database.'
