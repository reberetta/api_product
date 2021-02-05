import sys
sys.path.append('.')
import pytest
from pytest import raises
from backend.models.base_model import BaseModel
from backend.models.product import Product


@pytest.mark.parametrize("name, description, price", [('pname', 'pdescription', 44.99)])
def test_product_instance(name: str, description: str, price: float) -> None:
    product = Product(name, description, price)
    assert isinstance(product, Product)
    assert isinstance(product, BaseModel)
    assert product.name is name
    assert product.description is description
    assert product.price is price


@pytest.mark.parametrize("name, description, price", [('', 'pdescription', 44.99)])
def test_empty_name(name: str, description: str, price: float):
    with raises(ValueError):
        Product(name, description, price)


@pytest.mark.parametrize("name, description, price", [(789, 'pdescription', 44.99), (None, 'pdescription', 44.99)])
def test_error_type_name(name: str, description: str, price: float):
    with raises(TypeError):
        Product(name, description, price)


@pytest.mark.parametrize("name, description, price", [('pname'*21, 'pdescription', 44.99)])
def test_length_name(name: str, description: str, price: float):
    with raises(ValueError):
        Product(name, description, price)


@pytest.mark.parametrize("name, description, price", [('pname', 789, 44.99), ('pname', None, 44.99)])
def test_error_type_description(name: str, description: str, price: float):
    with raises(TypeError):
        Product(name, description, price)


@pytest.mark.parametrize("name, description, price", [('pname', 'pdescription'*22, 44.99)])
def test_length_description(name: str, description: str, price: float):
    with raises(ValueError):
        Product(name, description, price)


@pytest.mark.parametrize("name, description, price", [('pname', 'pdescription', -9.09)])
def test_negative_price(name: str, description: str, price: float):
    with raises(ValueError):
        Product(name, description, price)


@pytest.mark.parametrize("name, description, price", [('pname', 'pdescription', 'price'), ('pname', 'pdescription', None)])
def test_error_type_price(name: str, description: str, price: float):
    with raises(TypeError):
        Product(name, description, price)
