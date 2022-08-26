from src.utils.db_commands import create_db_and_tables, create_heroes, select_heroes


def main():
    create_db_and_tables()
    create_heroes()
    select_heroes()


if __name__ == "__main__":
    main()
