from sqlalchemy.orm import sessionmaker
from db.db import engine

Session = sessionmaker(bind=engine)
session = Session()
