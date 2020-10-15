from sqlalchemy import Column, Integer, String, Numeric

from db import Base


class OrderModel(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    currency = Column(String(30), nullable=False)
    amount = Column(Numeric, nullable=False)
    purchase_price = Column(Numeric, nullable=False)
    owner_id = Column(String(16), nullable=False)

    def __init__(self, currency=None, amount=None, purchase_price=None, owner_id=None):
        self.currency = currency
        self.amount = amount
        self.purchase_price = purchase_price
        self.owner_id = owner_id

    def __repr__(self):
        return '<Order {}>'.format(self.id)
