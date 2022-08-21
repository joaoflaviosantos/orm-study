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
        return f'User {self.name}'


def create_first_table():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_first_table()
