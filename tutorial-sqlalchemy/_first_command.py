from db.db import engine


def first_command():
    engine.execute('CREATE TABLE "EX1" ('
                   'id INTERGER NOT NULL,'
                   'name VARCHAR,'
                   'PRIMARY KEY (id));')


if __name__ == '__main__':
    first_command()
