from src.repository.actor_repository import ActorRepository
from src.repository.film_repository import FilmRepository


repo_film = FilmRepository()
repo_actor = ActorRepository()

insert = repo_film.insert('Test', 'Test', 2022)

update = repo_film.update('Test', 1994)

delete = repo_film.delete('Test')

print(repo_film.select())

print(repo_actor.select())

print(repo_film.select()[0].atores)
