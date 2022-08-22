from db.engine import engine

from models.product import Product
from models.user import User


def create_all_tables():
    print(f'\nCreate all tables:')
    User.__table__.create(engine)
    Product.__table__.create(engine)
