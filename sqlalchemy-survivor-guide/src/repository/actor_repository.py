from sqlalchemy.orm.exc import NoResultFound
from src.configs.connection import DBConnectionHandler
from src.models.model import Actor
from src.models.model import Film


class ActorRepository:

    def select(self):
        with DBConnectionHandler() as db:
            print(f'SELECT command:')
            try:
                data = db.session\
                    .query(Actor)\
                    .join(Film, Actor.titulo_filme == Film.titulo)\
                    .with_entities(
                        Actor.nome,
                        Film.titulo,
                        Film.genero)\
                    .all()
                return data
            except NoResultFound:
                return None
