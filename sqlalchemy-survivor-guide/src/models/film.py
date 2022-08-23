from src.configs.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Film(Base):
    __tablename__ = 'filmes'

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship('Actor', backref='atores', lazy='subquery')

    def __repr__(self) -> str:
        return f'Film: {self.titulo} | Genre: {self.genero} | Year: {self.ano}'
