from domeniu.clientFilm import ClientFilm
from domeniu.exceptii.duplicateError import DuplicateError
from repository.repository import Repository
from domeniu.dto.clientFilmDto import ClientSortareDTOAssembler, FilmSortareDTOAssembler, FilmSortareDTO, ClientSortareDTO

class ClientFilmService:
    def __init__(self, clientFilmRepository: Repository,
                 clientRepository: Repository,
                 filmRepository: Repository):
        self.__clientFilmRepository = clientFilmRepository
        self.__clientRepository = clientRepository
        self.__filmRepository = filmRepository

    def adaugaInchiriere(self, idClientFilm, idClient, idFilm):
        if self.__clientRepository.getById(idClient) is None:
            raise KeyError("Nu exista un client cu id-ul dat")
        if self.__filmRepository.getById(idFilm) is None:
            raise KeyError("Nu exista un film cu id-ul dat")
        inchirieri = self.__clientFilmRepository.getAll()

        for inchiriere in inchirieri:
            if inchiriere.getIdClient() == idClient and inchiriere.getIdFilm() == idFilm:
                raise DuplicateError("Clientul a inchiriat deja filmul dat")

        inchiriere = ClientFilm(idClientFilm, idClient, idFilm)
        self.__clientFilmRepository.adauga(inchiriere)

    def getAllInchirieri(self):
        return self.__clientFilmRepository.getAll()


    def stergeInchiriere(self, idClient, idFilm):
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() == idClient and inchiriere.getIdFilm == idFilm:
                self.__clientFilmRepository.sterge(inchiriere.getIdEntitate())

    def ordoneazaClientiDupaNume(self):
        clienti = self.__clientRepository.getAll()
        clientiDupaNume = []
        for client in clienti:
                clientiDupaNume.append(client)
        clientiDupaNume.sort(key= lambda client: client.getNume())
        return clientiDupaNume

    def ordoneazaClientiDupaNrFilme(self):
        clientiDupaNrInchirieri = {}
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() in clientiDupaNrInchirieri:
                clientiDupaNrInchirieri[inchiriere.getIdClient()] += 1
            else:
                clientiDupaNrInchirieri[inchiriere.getIdClient()] = 1
        idClientiOrdonati = sorted(clientiDupaNrInchirieri,
                               key = lambda idClient: clientiDupaNrInchirieri[idClient])
        clientiOrdonati = []
        for idClient in idClientiOrdonati:
            clientiOrdonati.append((idClient, clientiDupaNrInchirieri[idClient]))
        return clientiOrdonati

    def ordoneazaClientiDupaNrFilme30(self):
        clientiDupaNrInchirieri = {}
        cont = 0
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() in clientiDupaNrInchirieri:
                clientiDupaNrInchirieri[inchiriere.getIdClient()] += 1
            else:
                clientiDupaNrInchirieri[inchiriere.getIdClient()] = 1

        cont = len(clientiDupaNrInchirieri)

        idClientiOrdonati = sorted(clientiDupaNrInchirieri,
                                   key=lambda idClient: clientiDupaNrInchirieri[idClient],
                                   reverse=True)

        clientiOrdonati30 = []
        for idClient in idClientiOrdonati:
            if len(clientiOrdonati30) < (30 * cont / 100):
                clientiOrdonati30.append((idClient, clientiDupaNrInchirieri[idClient]))
        return clientiOrdonati30

    def ordoneazaFilmeDupaNrInchirieri(self):
        '''
        filmele sunt ordonate dupa nr de inchirieri
        :return:
        '''
        filmeDupaNrInchirieri = {}
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdFilm() in filmeDupaNrInchirieri:
                filmeDupaNrInchirieri[inchiriere.getIdFilm()] += 1
            else:
                filmeDupaNrInchirieri[inchiriere.getIdFilm()] = 1
        idFilmeOrdonate = sorted(filmeDupaNrInchirieri,
                               key = lambda idFilm: filmeDupaNrInchirieri[idFilm],
                               reverse = True)
        filmeOrdonate = []
        for idFilm in idFilmeOrdonate:
            if len(filmeOrdonate) <= 3:
                filmeOrdonate.append((idFilm, filmeDupaNrInchirieri[idFilm]))
        return filmeOrdonate

    def sortareFilmeDupaNrDeInchirieriDTO(self, filme, inchirieri):
        '''
        se apeleaza in sortareFilmeDupaNrDeInchirieri ce urmeaaza sa fie apelat in consola
        inlocuieste for-ul comentat in sortareFilmeDupaNrDeInchirieri
        :param filme:
        :return:
        '''
        rezultatFilme = {}
        for film in filme:
            rezultatFilme[film.getIdEntitate()] = FilmSortareDTOAssembler.create_film_dto(film, inchirieri)
        return rezultatFilme.values()

    def sortareFilmeDupaNrDeInchirieri(self):
        '''
        cele mai inchiriate filme
        :return:
        '''
        #rezultatFilme = {}
        inchirieri = self.__clientFilmRepository.getAll()
        filme = self.__filmRepository.getAll()
        '''for film in filme :
            nrClienti = 0
            for inchiriere in inchirieri :
                if film.getIdEntitate() == inchiriere.getIdFilm():
                    nrClienti += 1
            rezultatFilme[film.getIdEntitate()] = (film.getTitlu(), nrClienti)
        '''
        rezultatFilme = self.sortareFilmeDupaNrDeInchirieriDTO(filme, inchirieri)
        return sorted(rezultatFilme, key=lambda x: x.nume, reverse=False)

    def get30Filme(self):
        '''
        primii 30% clienti cu cele mai multe filme
        :return:
        '''

        list = self.sotrareClientiDupaNrDeFilmeInchiriate()
        result = []

        for i in range(int(len(list) * 0.3)):
            result.append(list.pop())
        return result

    def sotrareClientiDupaNrDeFilmeInchiriateDTO(self, clienti):
        rezultat = {}
        for client in clienti:
            rezultat[client.getIdEntitate()] = ClientSortareDTOAssembler()
        return rezultat.values()

    def sotrareClientiDupaNrDeFilmeInchiriate(self):
        '''
        clienti cu filme inchiriate ordonati dupa numarul de filme si dupa nume
        '''
        clienti = self.__clientRepository.getAll()
        inchirieri = self.__clientFilmRepository.getAll()
        #rezultat = {}
        '''
        for client in clienti:
            nrFilme = 0
            for inchiriere in inchirieri:
                if client.getIdEntitate() == inchiriere.getIdClient():
                    nrFilme = nrFilme + 1
            rezultat[client.getIdEntitate()] = ClientSortareDTO(client.getNume(), nrFilme)
        '''
        rezultat = [ClientSortareDTOAssembler.create_client_dto(client, inchirieri) for client in clienti]
        return sorted(rezultat, key=lambda x: (x.nume, x.nrFilme), reverse = False)

