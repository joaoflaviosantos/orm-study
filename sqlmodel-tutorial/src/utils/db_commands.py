import sys
import random
from sqlmodel import Session, select, or_

from src.db.db import engine, SQLModel
from src.models.hero import Hero
from src.models.team import Team

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
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain America", secret_name="Esteban Roger", age=93)

    with Session(engine) as session:
        try:
            session.add(hero_1)
            session.add(hero_2)
            session.add(hero_3)
            session.add(hero_4)
            session.add(hero_5)
            session.add(hero_6)
            session.add(hero_7)
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


def select_heroes_with_limit():
    with Session(engine) as session:
        try:
            heros = session.exec(select(Hero).limit(3)).all()
            print("\nHeros:", heros)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])


def select_heroes_with_offset_and_limit():
    with Session(engine) as session:
        try:
            heros = session.exec(select(Hero).offset(3).limit(3)).all()
            print("\nHeros:", heros)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])


def update_heroes():
    with Session(engine) as session:
        try:
            hero_1 = session.exec(select(Hero).where(
                Hero.name == "Spider-Boy")).one()
            print("\nHero 1:", hero_1)

            hero_1.age = 16
            hero_1.name = "Spider-Youngster"
            session.add(hero_1)

            hero_2 = session.exec(select(Hero).where(
                Hero.name == "Captain America")).one()
            print("\nHero 2:", hero_2)

            hero_2.age = int(random.uniform(15, 50))
            # hero_2.name="Captain North America Except Canada"
            session.add(hero_2)

            session.commit()
            session.refresh(hero_1)
            session.refresh(hero_2)

            print("\nUpdated hero 1:", hero_1)
            print("\nUpdated hero 2:", hero_2)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])
            session.rollback()


def delete_heroes():
    with Session(engine) as session:
        try:
            hero = session.exec(select(Hero).where(
                Hero.name == "Spider-Youngster")).one()
            print("\nHero: ", hero)

            session.delete(hero)
            session.commit()
            print("\nDeleted hero:", hero)

            hero = session.exec(select(Hero).where(
                Hero.name == "Spider-Youngster")).first()

            if hero is None:
                print("\nThere's no hero named Spider-Youngster")
        except:
            print("\nUnexpected error:", sys.exc_info()[0])
            session.rollback()


def create_heroes_with_teams():
    with Session(engine) as session:
        try:
            team_preventers = Team(
                name="Preventers", headquarters="Sharp Tower")
            team_z_force = Team(
                name="Z-Force", headquarters="Sister Margaret’s Bar")
            session.add(team_preventers)
            session.add(team_z_force)
            session.commit()

            hero_deadpond = Hero(
                name="Deadpond", secret_name="Dive Wilson", team_id=team_z_force.id
            )
            hero_rusty_man = Hero(
                name="Rusty-Man",
                secret_name="Tommy Sharp",
                age=48,
                team_id=team_preventers.id,
            )
            hero_spider_boy = Hero(
                name="Spider-Boy", secret_name="Pedro Parqueador")
            hero_youngster = Hero(
                name="Spider-Youngster", secret_name="Youngster Deleted")
            session.add(hero_deadpond)
            session.add(hero_rusty_man)
            session.add(hero_spider_boy)
            session.add(hero_youngster)
            session.commit()

            session.refresh(hero_deadpond)
            session.refresh(hero_rusty_man)
            session.refresh(hero_spider_boy)
            session.refresh(hero_youngster)

            print("\nCreated hero:", hero_deadpond)
            print("\nCreated hero:", hero_rusty_man)
            print("\nCreated hero:", hero_spider_boy)
            print("\nCreated hero:", hero_youngster)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])
            session.rollback()


def select_heroes_with_implicit_join():
    with Session(engine) as session:
        try:
            results = session.exec(
                select(Hero, Team).where(Hero.team_id == Team.id))
            for hero, team in results:
                print("\nHero:", hero, "Team:", team)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])
            session.rollback()


def select_heroes_with_explicit_join():
    with Session(engine) as session:
        try:
            results = session.exec(select(Hero, Team).join(Team))
            for hero, team in results:
                print("\nHero:", hero, "Team:", team)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])
            session.rollback()


def select_heroes_with_left_outer_join():
    with Session(engine) as session:
        try:
            results = session.exec(select(Hero, Team).join(Team, isouter=True))
            for hero, team in results:
                print("\nHero:", hero, "Team:", team)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])
            session.rollback()


def select_heroes_with_explicit_join_and_where():
    with Session(engine) as session:
        try:
            results = session.exec(select(Hero, Team).join(
                Team).where(Team.name == "Preventers"))
            for hero, team in results:
                print("\nHero:", hero, "Team:", team)
        except:
            print("\nUnexpected error:", sys.exc_info()[0])
            session.rollback()
