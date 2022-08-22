from _create_first_table import User
from db.orm import session


def class_method_query():
    query = User.find_by_name(session, 'Ana')
    print(query.all())


if __name__ == '__main__':
    class_method_query()
