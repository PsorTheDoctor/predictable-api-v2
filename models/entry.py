from sqlalchemy import Column, Integer, String

from db import Base


class EntryModel(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    header = Column(String(200), nullable=False)
    link = Column(String(200), nullable=False)
    date = Column(String(30), nullable=False)
    tag = Column(String(30))

    def __init__(self, header=None, link=None, date=None, tag=None):
        self.header = header
        self.link = link
        self.date = date
        self.tag = tag

    def __repr__(self):
        return '<News {} {}>'.format(self.tag, self.id)
