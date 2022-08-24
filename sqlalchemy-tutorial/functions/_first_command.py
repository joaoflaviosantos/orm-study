from db.engine import engine


def first_command():
    print(f'\nFirst command:')
    engine.execute('CREATE TABLE "EX1" ('
                   'id INTERGER NOT NULL,'
                   'name VARCHAR,'
                   'PRIMARY KEY (id));')
