from src.configs.connection import DBConnectionHandler
from src.models.film import Film


class FilmRepository:

    def select(self):
        with DBConnectionHandler() as db:
            print(f'SELECT command:')
            data = db.session.query(Film).all()
            return data

    def insert(self, title, genre, year):
        with DBConnectionHandler() as db:
            print(f'INSERT command:')
            data_insert = Film(titulo=title, genero=genre, ano=year)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, title):
        with DBConnectionHandler() as db:
            print(f'DELETE command:')
            data = db.session.query(Film).filter(Film.titulo == title).delete()
            db.session.commit()

    def update(self, title, year):
        with DBConnectionHandler() as db:
            print(f'UPDATE command:')
            db.session.query(Film).filter(
                Film.ano == title).update({"ano": year})
            db.session.commit()
