from sqlalchemy import Column, String, Float
from sqlalchemy.orm import validates

from backend.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'PRODUCT'

    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)
    price = Column('price', Float, nullable=False)

    def __init__(self, name: str, description: str, price: float) -> None:
        self.name = name
        self.description = description
        self.price = price

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('Name must be string.')
        if not name.strip():
            raise ValueError('Name cannot be empty.')
        if len(name) > 100:
            raise ValueError('Name cannot be longer than 100 characters.')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError('Description must be string.')
        if len(description) > 255:
            raise ValueError('Description cannot be longer than 255 characters.')
        return description

    @validates('price')
    def validate_price(self, key, price):
        if not isinstance(price, float):
            raise TypeError('Price must be float.')
        if price < 0.0:
            raise ValueError('Price cannot be negative.')
        return price
