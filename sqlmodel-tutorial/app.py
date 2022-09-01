from src.utils import commons
from src.utils import db_commands


def main():
    commons.exclusion_db()
    db_commands.create_db_and_tables()
    db_commands.create_heroes_with_teams()
    db_commands.select_heroes()
    db_commands.select_heroes_with_simple_where()
    db_commands.select_heroes_with_and_where()
    db_commands.select_heroes_with_or_where()
    db_commands.select_heroes_with_first()
    db_commands.select_heroes_with_one()
    db_commands.select_heroes_with_get()
    db_commands.select_heroes_with_limit()
    db_commands.select_heroes_with_offset_and_limit()
    db_commands.update_heroes()
    db_commands.delete_heroes()
    db_commands.select_heroes_with_implicit_join()
    db_commands.select_heroes_with_explicit_join()
    db_commands.select_heroes_with_left_outer_join()
    db_commands.select_heroes_with_explicit_join_and_where()
    db_commands.create_heroes_team_relationship()
    db_commands.remove_heroes_team_relationship()


if __name__ == "__main__":
    main()
