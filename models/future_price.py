from sqlalchemy import Column, Integer, String, Numeric

from db import Base


class FuturePriceModel(Base):
    __tablename__ = 'future_prices'

    id = Column(Integer, primary_key=True)
    currency = Column(String(50), nullable=False)
    n_days_forward = Column(Integer, nullable=False)
    value = Column(Numeric, nullable=False)

    def __init__(self, currency=None, n_days_forward=None, value=None):
        self.currency = currency
        self.n_days_forward = n_days_forward
        self.value = value

    def __repr__(self):
        return '<Future {} price>'.format(self.currency)
