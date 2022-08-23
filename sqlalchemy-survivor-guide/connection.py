from sqlalchemy import create_engine

engine = create_engine('sqlite:///cinema.db', echo=True)
conn = engine.connect()
#response = conn.execute('SELECT * FROM filmes;')
response = engine.execute('SELECT * FROM filmes;')

for row in response:
    print(row)
