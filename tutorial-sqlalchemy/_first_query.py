from _create_first_table import User
from db.orm import session


def first_query():
    #query = session.query(User).filter_by(name='John')
    #query = session.query(User).filter(User.name == 'John').first()
    query = session.query(User).filter(User.name.like('%John%'))
    print(query.all())
    print(query.count())


if __name__ == '__main__':
    first_query()
