from src.configs.base import Base
from sqlalchemy import Column, Integer, String


class Film(Base):
    __tablename__ = 'filmes'

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f'Film: {self.titulo} | Genre: {self.genero} | Year: {self.ano}'
