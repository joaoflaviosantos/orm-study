from sqlalchemy.orm.exc import NoResultFound
from src.models.model import Film


class FilmRepository:
    
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler

    def select(self):
        with self.__ConnectionHandler() as db:
            print(f'SELECT command:')
            try:
                data = db.session.query(Film).all()
                return data
            except NoResultFound:
                return None

    def select_with_genre_filter(self, genre):
        with self.__ConnectionHandler() as db:
            print(f'SELECT command:')
            try:
                data = db.session.query(Film).filter(
                    Film.genero == genre).first()
                return data
            except NoResultFound:
                return None

    def insert(self, title, genre, year):
        with self.__ConnectionHandler() as db:
            print(f'INSERT command:')
            try:
                data_insert = Film(titulo=title, genero=genre, ano=year)
                db.session.add(data_insert)
                db.session.commit()
                db.session.refresh(data_insert)
                return data_insert
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, title):
        with self.__ConnectionHandler() as db:
            print(f'DELETE command:')
            try:
                data = db.session.query(Film).filter(
                    Film.titulo == title).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, title, year):
        with self.__ConnectionHandler() as db:
            print(f'UPDATE command:')
            try:
                db.session.query(Film).filter(
                    Film.ano == title).update({"ano": year})
                db.session.commit()
                return 
            except Exception as exception:
                db.session.rollback()
                raise exception
