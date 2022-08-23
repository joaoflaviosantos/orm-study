from src.configs.connection import DBConnectionHandler
from src.models.actor import Actor
from src.models.film import Film


class ActorRepository:

    def select(self):
        with DBConnectionHandler() as db:
            print(f'SELECT command:')
            data = db.session\
                .query(Actor)\
                .join(Film, Actor.titulo_filme == Film.titulo)\
                .with_entities(
                    Actor.nome,
                    Film.titulo,
                    Film.genero)\
                .all()
            return data
