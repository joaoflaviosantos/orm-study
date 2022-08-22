import imp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from db.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'Id: {self.id} | User: {self.name}'

    @classmethod
    def find_by_name(cls, session, name):
        query = session.query(cls).filter(cls.name.like(f'%{name}%'))
        return query


def create_first_table():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_first_table()
