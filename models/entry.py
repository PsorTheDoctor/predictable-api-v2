from sqlalchemy import Column, Integer, String

from db import Base


class EntryModel(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    header = Column(String(200), nullable=False)
    publisher = Column(String(30), nullable=False)
    content = Column(String(200), nullable=False)
    link = Column(String(200), nullable=False)
    n_days_ago = Column(String(30), nullable=False)
    img = Column(String(90), nullable=False)

    def __init__(self, header=None, publisher=None, content=None, link=None, n_days_ago=None, img=None):
        self.header = header
        self.publisher = publisher
        self.content = content
        self.link = link
        self.n_days_ago = n_days_ago
        self.img = img

    def __repr__(self):
        return '<News {}>'.format(self.id)
