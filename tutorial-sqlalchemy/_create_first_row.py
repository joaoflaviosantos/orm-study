from _create_first_table import User
from db.orm import session


def create_first_row():
    user = User(name='John Snow', password='johnspassword')
    session.add(user)
    session.commit()
    print(user.id)


if __name__ == '__main__':
    create_first_row()
