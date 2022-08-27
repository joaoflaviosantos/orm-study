import sys
from sqlmodel import Session, select, or_

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
            print("\nUnexpected error:", sys.exc_info()[0])
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
            print("\nUnexpected error:", sys.exc_info()[0])
            session.rollback()

    print("\nAfter the session closes")
    print("Hero 1:", hero_1)
    print("Hero 2:", hero_2)
    print("Hero 3:", hero_3)


def select_heroes():
    with Session(engine) as session:
        try:
            heroes = session.exec(select(Hero)).all()
            print()
            print(heroes)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])


def select_heroes_with_simple_where():
    with Session(engine) as session:
        try:
            heroes = session.exec(select(Hero).where(
                Hero.name == "Deadpond")).all()
            print()
            print(heroes)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])


def select_heroes_with_and_where():
    with Session(engine) as session:
        try:
            heroes = session.exec(select(Hero).where(
                Hero.age >= 48, Hero.age < 50)).all()
            print()
            print(heroes)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])


def select_heroes_with_or_where():
    with Session(engine) as session:
        try:
            heroes = session.exec(select(Hero).where(
                or_(Hero.age <= 50, Hero.age > 90))).all()
            print()
            print(heroes)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])


def select_heroes_with_first():
    with Session(engine) as session:
        try:
            hero = session.exec(select(Hero).where(Hero.name == None)).first()
            print("\nHero:", hero)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])


def select_heroes_with_one():
    with Session(engine) as session:
        try:
            hero = session.exec(select(Hero).where(Hero.name == None)).one()
            print("\nHero:", hero)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])


def select_heroes_with_get():
    with Session(engine) as session:
        try:
            hero = session.get(Hero, 1)
            print("\nHero:", hero)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])
