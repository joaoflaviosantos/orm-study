from sqlmodel import Session

from src.db.db import engine, SQLModel
from src.models.hero import Hero


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        try:
            session.add(hero_1)
            session.add(hero_2)
            session.add(hero_3)
            session.commit()
        except:
            session.rollback()
