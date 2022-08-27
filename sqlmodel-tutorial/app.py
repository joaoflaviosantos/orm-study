from src.utils import commons
from src.utils import db_commands


def main():
    commons.exclusion_db()
    db_commands.create_db_and_tables()
    db_commands.create_heroes()
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


if __name__ == "__main__":
    main()
