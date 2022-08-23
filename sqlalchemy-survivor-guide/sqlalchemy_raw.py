import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Configs
engine = create_engine('sqlite:///cinema.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Entities
class Film(Base):
    __tablename__ = 'filmes'

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f'Film: {self.titulo} | Genre: {self.genero} | Year: {self.ano}'


# SQL
# Insert
try:
    data_insert = Film(titulo='Batman Begins', genero='Ação', ano=2006)
    session.add(data_insert)
    session.commit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    session.rollback()

# Update
try:
    session.query(Film).filter(
        Film.titulo == 'Batman Begins').update({"ano": 2000})
    session.commit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    session.rollback()

# Delete
try:
    session.query(Film).filter(Film.titulo == 'Batman Begins').delete()
    session.commit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    session.rollback()

# Select
try:
    data = session.query(Film).all()
    print(data)
except:
    print("Unexpected error:", sys.exc_info()[0])

session.close()
