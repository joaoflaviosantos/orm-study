from src.repository.film_repository import FilmRepository

repo = FilmRepository()

insert = repo.insert('Test', 'Test', 2022)

update = repo.update('Test', 1994)

delete = repo.delete('Test')

print(repo.select())
