from src.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Actor(Base):
    __tablename__ = 'atores'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    titulo_filme = Column(String, ForeignKey('filmes.titulo'))

    def __repr__(self) -> str:
        return f'Actor: {self.nome} | Film: {self.titulo_filme}'

class Film(Base):
    __tablename__ = 'filmes'

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship('Actor', backref='atores', lazy='subquery')

    def __repr__(self) -> str:
        return f'Film: {self.titulo} | Genre: {self.genero} | Year: {self.ano}'
