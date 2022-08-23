import sqlite3
from sqlalchemy import create_engine

connection = sqlite3.connect('cinema.db')
connection.close()

engine = create_engine('sqlite:///cinema.db', echo=True)
conn = engine.connect()

conn.execute('''
CREATE TABLE IF NOT EXISTS filmes (
    titulo VARCHAR(50) PRIMARY KEY,
    genero VARCHAR(30) NOT NULL,
    ano INTEGER NOT NULL
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS atores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL,
    titulo_filme VARCHAR(50) NOT NULL,
    FOREIGN KEY (titulo_filme) REFERENCES filmes(titulo)
);
''')

conn.execute('''
INSERT INTO filmes (titulo, genero, ano)
VALUES ("Forest Gump", "Drama", 1994);
''')

conn.execute('''
INSERT INTO atores (nome, titulo_filme)
VALUES ("Tom Hanks", "Forest Gump");
''')
