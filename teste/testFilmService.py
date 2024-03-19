#from domeniu.filmValidator import FilmValidator
from repository.repository import Repository
from service.FilmService import FilmService


def testAdaugaFilmSevice():
    filmRepository = Repository()
    clientFilmRpository = Repository()
    #filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, clientFilmRpository) #filmValidator)
    filmService.adaugaFilm("1", "Stalingrad", "film despre batalia de la Stalingerad", "istoric")

    filme = filmService.getAllFilme()
    assert len(filme) == 1
    assert filme[0].getIdEntitate() == "1"



def testModificaFilmService():
    filmRepository = Repository()
    clientFilmRpository = Repository()
    #filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, clientFilmRpository) #filmValidator)
    filmService.adaugaFilm("1", "Stalingrad", "film despre batalia de la Stalingerad", "istoric")

    filmService.modificaFilm("1", "Moartea lui Stalin", "film despre URSS", "istoric")

    filme = filmService.getAllFilme()
    assert filme[0].getTitlu() == "Moartea lui Stalin"



def testStergeFilmService():
    filmRepository = Repository()
    clientFilmRepository = Repository()
    #filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, clientFilmRepository) #filmValidator)
    filmService.adaugaFilm("1", "Stalingrad", "film despre batalia de la Stalingerad", "istoric")

    filmService.stergeFilm("1")

    filme = filmService.getAllFilme()
    assert len(filme) == 0

