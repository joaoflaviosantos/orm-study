from unittest import mock
from urllib import response
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.model import Film
from src.repository.film_repository import FilmRepository

class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Film)],
                    [Film(titulo="Alice", genero="Test", ano=1996)]
                ),
                (
                    [
                        mock.call.query(Film),
                        mock.call.filter(Film.genero=="Anything")
                    ],
                    [Film(titulo="John", genero="Anything", ano=1996)]
                )
            ]
        )

    def __enter__(self):
        print('\n-------- OPENING THE SESSION --------')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('-------- CLOSING THE SESSION --------\n')
        self.session.close()


def test_select():
    film_repository = FilmRepository(ConnectionHandlerMock)
    response = film_repository.select()
    print()
    print(response)
    assert isinstance(response, list)
    assert isinstance(response[0], Film)

def test_select_genero_drama():
    film_repository = FilmRepository(ConnectionHandlerMock)
    response = film_repository.select_with_genre_filter("Anything")
    print()
    print(response)
    assert isinstance(response, Film)
    assert response.titulo == "John"

def test_insert():
    film_repository = FilmRepository(ConnectionHandlerMock)
    response = film_repository.insert('Something', 'Horror', 1998)
    print()
    print(response)
