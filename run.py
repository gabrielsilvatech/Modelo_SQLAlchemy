from infra.repository.atores_repository import AtoresRepository
from infra.repository.filmes_repository import FilmesRepository
from infra.configs.connection import DBConnectionHandler

#repo = AtoresRepository()
#response = repo.select()
#print(response)


repo2 = FilmesRepository(DBConnectionHandler)
response2 = repo2.select_drama_filmes()
print(response2)