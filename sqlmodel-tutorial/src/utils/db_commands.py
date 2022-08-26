import sys
from sqlmodel import Session, select

from src.db.db import engine, SQLModel
from src.models.hero import Hero

from sqlmodel.sql.expression import Select, SelectOfScalar

# https://github.com/tiangolo/sqlmodel/issues/189#issuecomment-1025190094
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


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
            print("Unexpected error:", sys.exc_info()[0].__dict__)
            session.rollback()


def create_heroes_what_goes_back():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        try:
            session.add(hero_1)
            session.add(hero_2)
            session.add(hero_3)

            print("\nAfter adding to the session")
            print("Hero 1:", hero_1)
            print("Hero 2:", hero_2)
            print("Hero 3:", hero_3)

            session.commit()

            print("\nAfter committing the session")
            print("Hero 1:", hero_1)
            print("Hero 2:", hero_2)
            print("Hero 3:", hero_3)

            print("\nAfter committing the session, show IDs")
            print("Hero 1 ID:", hero_1.id)
            print("Hero 2 ID:", hero_2.id)
            print("Hero 3 ID:", hero_3.id)

            print("\nAfter committing the session, show names")
            print("Hero 1 name:", hero_1.name)
            print("Hero 2 name:", hero_2.name)
            print("Hero 3 name:", hero_3.name)

            session.refresh(hero_1)
            session.refresh(hero_2)
            session.refresh(hero_3)

            print("\nAfter refreshing the heroes")
            print("Hero 1:", hero_1)
            print("Hero 2:", hero_2)
            print("Hero 3:", hero_3)

        except:
            print("Unexpected error:", sys.exc_info()[0].__dict__)
            session.rollback()

    print("\nAfter the session closes")
    print("Hero 1:", hero_1)
    print("Hero 2:", hero_2)
    print("Hero 3:", hero_3)


def select_heroes():
    with Session(engine) as session:
        try:
            heroes = session.exec(select(Hero)).all()
            print(heroes)
        except:
            print("Unexpected error:", sys.exc_info()[0])
