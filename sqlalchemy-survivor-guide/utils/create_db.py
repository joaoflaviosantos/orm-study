import sqlite3
from sqlalchemy import create_engine

connection = sqlite3.connect('cinema.db')
connection.close()

engine = create_engine('sqlite:///cinema.db', echo=True)
conn = engine.connect()

conn.execute('''
CREATE TABLE IF NOT EXISTS filmes (
    titulo VARCHAR(50) NOT NULL,
    genero VARCHAR(30) NOT NULL,
    ano INT NOT NULL,
    PRIMARY KEY(titulo)
);
''')

conn.execute('''
INSERT INTO filmes (titulo, genero, ano)
VALUES ("Forest Gump", "Drama", 1994);
''')
