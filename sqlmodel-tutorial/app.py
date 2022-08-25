from src.db.db import engine, SQLModel

SQLModel.metadata.create_all(engine)
