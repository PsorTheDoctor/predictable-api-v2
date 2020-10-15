from sqlalchemy import Column, Integer, String, Numeric

from db import Base


class OrderModel(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    currency = Column(String(30), nullable=False)
    amount = Column(Numeric, nullable=False)
    purchasePrice = Column(Numeric, nullable=False)
    ownerId = Column(String(16), nullable=False)

    def __init__(self, currency=None, amount=None, purchasePrice=None, ownerId=None):
        self.currency = currency
        self.amount = amount
        self.purchasePrice = purchasePrice
        self.ownerId = ownerId

    def __repr__(self):
        return '<Order {}>'.format(self.id)
