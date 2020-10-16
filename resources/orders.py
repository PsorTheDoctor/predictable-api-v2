from flask_restful import Resource, reqparse, fields, marshal_with

from models.order import OrderModel
from db import db_session

parser = reqparse.RequestParser()
parser.add_argument('currency', type=str, required=True)
parser.add_argument('amount', type=float, required=True)
parser.add_argument('purchase_price', type=float, required=True)
parser.add_argument('owner_id', type=str, required=True)


resource_fields = {
    'id': fields.Integer,
    'currency': fields.String,
    'amount': fields.Float,
    'purchase_price': fields.Float,
    'owner_id': fields.String
}


class OrderList(Resource):
    @marshal_with(resource_fields)
    def get(self, owner_id):
        return OrderModel.query.filter_by(owner_id=owner_id).all()

    @marshal_with(resource_fields)
    def post(self, owner_id):
        args = parser.parse_args()
        order = OrderModel(currency=args['currency'],
                           amount=args['amount'],
                           purchase_price=args['purchase_price'],
                           owner_id=owner_id)  # args['owner_id']
        db_session.add(order)
        db_session.commit()
        return '', 201


class Order(Resource):
    @marshal_with(resource_fields)
    def delete(self, order_id):
        order = OrderModel.query.filter_by(id=order_id).first()
        db_session.delete(order)
        db_session.commit()
        return '', 204
