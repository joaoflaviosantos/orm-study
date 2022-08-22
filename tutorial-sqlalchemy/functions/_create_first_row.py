from models.user import User
from db.orm import session


def create_first_row():
    print(f'\nCreate first row:')
    user = User(name='John Snow', password='johnspassword')
    session.add(user)
    session.commit()
    print(user.id)
