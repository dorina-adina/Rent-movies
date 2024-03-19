from repository.repository import Repository
from service.ClientService import ClientService
from service.FilmService import FilmService
from service.clientFilmService import ClientFilmService
from ui.consola1 import Consola
from repository.fileRepository import FileClientRepository
#from domeniu.filmValidator import FilmValidator


def main():
    #testAll()

    clientFileRepository = FileClientRepository("clienti.txt")
    filmRepository = Repository()
    clientFilmRepository = Repository()
    #filmValidator = FilmValidator()

    clientService = ClientService(clientFileRepository, clientFilmRepository)

    filmService = FilmService(filmRepository, clientFilmRepository) #filmValidator)

    clientFilmService = ClientFilmService(clientFilmRepository, clientFileRepository, filmRepository)

    consola1 = Consola(clientService, filmService, clientFilmService)

    consola1.meniu()

    client1 = Client(1, "Popescu Mara", 6789)
    client2 = Client(2, "Barbu Dana", 8904)
    client3 = Client(3, "Pascu Andrei", 4567)
    repository.adauga(client1)
    repository.adauga(client2)
    repository.adauga(client3)

    film1 = Film(101, "Pe aripile vantului", "drama", "ok")
    film2 = Film(102, "Stalingrad", "istric", "ok")
    repository.adauga(film1)
    repository.adauga(film2)

    inchiriere1 = Inchiriere(133, 1, 101)
    inchiriere2 = Inchiriere(233, 3, 102)
    inchiriere3 = Inchiriere(333, 1, 102)

    repository.adauga(inchiriere1)
    repository.adauga(inchiriere2)
    repository.adauga(inchiriere3)


main()