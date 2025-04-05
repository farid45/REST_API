from itertools import product

from flask import Flask, request, jsonify
from marshmallow import ValidationError
from pip._internal.configuration import Configuration

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.businsess_logic.product import Product
from eshop.businsess_logic.product_usecases import product_create, product_get_by_id, product_get_many
from eshop.data_access.product_repo import get_many
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from eshop.view.prod_schemas import ProdSchema, ProdGetManyParams

app = Flask(__name__)


@app.post("/api/v1/order")
def order_create_endpoint():
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)
@app.route('/products', methods=['GET'])
def get_products():
    return product_get_many()

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id:str):
    get_prod = product_get_by_id(product_id)
    if get_prod is None:
        return {
            "error": 'NOT FOUND'
        }, 404

    return ProdSchema().dump(get_prod)

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    print(data)
    if 'id' not in data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Отсутствуют обязательные поля'}), 400

    product_create(data['id'], data['name'], data['price'])
    get_pr = product_get_by_id(data['id'])
    return ProdSchema().dump(get_pr)





@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id):
    order = order_get_by_id(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)


def run_server():
    app.run()
