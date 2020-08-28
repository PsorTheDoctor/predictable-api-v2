from flask_restful import Resource, abort, fields, marshal_with

from models.future_price import FuturePriceModel
from db import db_session
from utils.machine_learning import *

resource_fields = {
    'id': fields.Integer,
    'currency': fields.String,
    'n_days_forward': fields.String,
    'value': fields.Float
}


class FuturePriceList(Resource):
    @marshal_with(resource_fields)
    def get(self, currency):
        response = FuturePriceModel.query.filter_by(currency=currency).all()
        if not response:
            abort(404, message='No data')
        return response


class FuturePrice(Resource):
    @marshal_with(resource_fields)
    def get(self, currency, n_days_forward):
        response = FuturePriceModel.query.filter_by(currency=currency).filter_by(n_days_forward=n_days_forward).first()

        if not response:
            predict_prices(currency, n_last_days=30, n_future_days=n_days_forward)
            value = get_single_future_price(n_days_forward)
            price = FuturePriceModel(currency, n_days_forward, value)
            db_session.add(price)
            db_session.commit()
            response = price
        return response
