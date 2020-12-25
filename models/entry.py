from sqlalchemy import Column, Integer, String

from db import Base


class EntryModel(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    header = Column(String(200), nullable=False)
    publisher = Column(String(30), nullable=False)
    link = Column(String(200), nullable=False)
    date = Column(String(30), nullable=False)

    def __init__(self, header=None, publisher=None, link=None, date=None):
        self.header = header
        self.publisher = publisher
        self.link = link
        self.date = date

    def __repr__(self):
        return '<News {}>'.format(self.id)
