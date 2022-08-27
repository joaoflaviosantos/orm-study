from src.utils.db_commands import create_db_and_tables,\
    create_heroes,\
    select_heroes,\
    select_heroes_with_simple_where,\
    select_heroes_with_and_where,\
    select_heroes_with_or_where,\
    select_heroes_with_first,\
    select_heroes_with_one,\
    select_heroes_with_get,\
    select_heroes_with_limit,\
    select_heroes_with_offset_and_limit


def main():
    create_db_and_tables()
    create_heroes()
    select_heroes()
    select_heroes_with_simple_where()
    select_heroes_with_and_where()
    select_heroes_with_or_where()
    select_heroes_with_first()
    select_heroes_with_one()
    select_heroes_with_get()
    select_heroes_with_limit()
    select_heroes_with_offset_and_limit()


if __name__ == "__main__":
    main()
