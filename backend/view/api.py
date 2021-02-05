import sys
sys.path.append('.')

from flask import Flask
from flask_restful import Api
from backend.resources.product_resource import ProductResource


app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/api/products/', endpoint='products')
api.add_resource(ProductResource, '/api/products/<int:id>/', endpoint='product')


app.run(debug=True, port=5005)
