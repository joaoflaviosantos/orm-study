from models.user import User
from db.orm import session


def first_query():
    print(f'\nCall first query:')
    #query = session.query(User).filter_by(name='John')
    #query = session.query(User).filter(User.name == 'John').first()
    query = session.query(User).filter(User.name.like('%John%'))
    print(query.all())
