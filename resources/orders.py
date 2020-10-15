from flask_restful import Resource, reqparse, fields, marshal_with

from models.order import OrderModel
from db import db_session

parser = reqparse.RequestParser()
parser.add_argument('currency', type=str, required=True)
parser.add_argument('amount', type=float, required=True)
parser.add_argument('purchasePrice', type=float, required=True)
parser.add_argument('ownerId', type=str, required=True)


resource_fields = {
    'id': fields.Integer,
    'currency': fields.String,
    'amount': fields.Float,
    'purchasePrice': fields.Float,
    'ownerId': fields.String
}


class OrderList(Resource):
    @marshal_with(resource_fields)
    def get(self, ownerId):
        return OrderModel.query.filter_by(ownerId=ownerId).all()


class Order(Resource):
    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        order = OrderModel(currency=args['currency'],
                           amount=args['amount'],
                           purchasePrice=args['purchasePrice'],
                           ownerId=args['ownerId'])
        db_session.add(order)
        db_session.commit()
        return '', 201

    @marshal_with(resource_fields)
    def delete(self, orderId):
        order = OrderModel.query.filter_by(id=orderId).first()
        db_session.delete(order)
        db_session.commit()
        return '', 204
