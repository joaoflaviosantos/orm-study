from db.connection import conn


def command_with_conn():
    print(f'\nCommand with connection:')
    trans = conn.begin()
    conn.execute('INSERT INTO "EX1" (id, name) '
                 'VALUES (1, "Hello")')
    trans.commit()


if __name__ == '__main__':
    command_with_conn()
