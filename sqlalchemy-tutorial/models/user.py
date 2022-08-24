from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.product import Product

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    #products = relationship(Product, backref="users")

    def __repr__(self):
        return f'Id: {self.id} | User: {self.name}'

    @classmethod
    def find_by_name(cls, session, name):
        query = session.query(cls).filter(cls.name.like(f'%{name}%'))
        return query
