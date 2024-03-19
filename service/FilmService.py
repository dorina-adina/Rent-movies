from domeniu.film import Film
#from domeniu.filmValidator import FilmValidator
from repository.repository import Repository


class FilmService:
    def __init__(self, filmRepository: Repository, clientFilmRepository: Repository): #filmValidator: FilmValidator):
        ''''filmValidator: FilmValidator'''
        self.__filmRepository = filmRepository
        self.__clientFilmRepository = clientFilmRepository
        #self.__filmValidator = filmValidator

    def getAllFilme(self):
        '''
        returneaza lista de filme
        :return: o lista de obiecte de tipul Film
        '''
        return self.__filmRepository.getAll()

    def adaugaFilm(self, idFilm, titlu, descriere, gen):
        '''
        adauga un film
        :param idFilm: string
        :param titlu: string
        :param descriere: string
        :param gen: string
        :return:
        '''
        film = Film(idFilm, titlu, descriere, gen)
        #self.__filmValidator.valideaza(film)
        self.__filmRepository.adauga(film)

    def modificaFilm(self, idFilm ,titluNou, descriereNoua, genNou):
        '''
        modifica un film dupa id
        :param idFilm: string
        :param titluNou: string
        :param descriereNoua: string
        :param genNou: string
        :return:
        '''
        filmNou = Film(idFilm, titluNou, descriereNoua, genNou)
        #self.__filmValidator.valideaza(filmNou)
        self.__filmRepository.modifica(filmNou)

    def stergeFilm(self, idFilm):
        '''
        sterge un film dupa id
        :param idFilm: string
        :return:
        '''
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdFilm() == idFilm:
                self.__clientFilmRepository.sterge(inchiriere.getIdEntitate())

        self.__filmRepository.sterge(idFilm)


