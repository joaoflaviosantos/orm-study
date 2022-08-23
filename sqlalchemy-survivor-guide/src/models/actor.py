from src.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Actor(Base):
    __tablename__ = 'atores'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    titulo_filme = Column(String, ForeignKey('filmes.titulo'))

    def __repr__(self) -> str:
        return f'Actor: {self.nome} | Film: {self.titulo_filme}'
