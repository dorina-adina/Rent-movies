from domeniu.client import Client
from repository.repository import Repository


class ClientService:
    def __init__(self, clientRepository: Repository, clientFilmRepository: Repository):
        self.__clientRepository = clientRepository
        self.__clientFilmRepository = clientFilmRepository

    def getAllClienti(self):
        '''
        returneaza lista de clienti
        :return: o lista de obiecte de tipul Client
        '''
        return self.__clientRepository.getAll()

    def adauga(self, idClient, nume, cnp):
        '''
        adauga un client
        :param idClient: string
        :param nume: string
        :param cnp: string

        :return:
        '''

        client = Client(idClient, nume, cnp)
        self.__clientRepository.adauga(client)

    def modifica(self, idClient, numeNou, cnp):
        '''
        modifica un client dupa id
        :param idClient: string
        :param numeNou: string
        :param cnp: string
        :return:
        '''

        clientNou = Client(idClient, numeNou, cnp)
        self.__clientRepository.modifica(clientNou)

    def sterge(self, idClient):
        ''''
        sterge un angajat dupa id
        :param idClient: string
        :return:
        '''
        inchirieri = self.__clientFilmRepository.getAll()
        for inchiriere in inchirieri:
            if inchiriere.getIdClient() == idClient:
                self.__clientFilmRepository.sterge(inchiriere.getIdEntitate())

        self.__clientRepository.sterge(idClient)



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
                                   key = lambda idClient: clientiDupaNrInchirieri[idClient],
                                   reverse = True)

        clientiOrdonati30 = []
        for idClient in idClientiOrdonati:
            if len(clientiOrdonati30) < (30*cont/100):
                clientiOrdonati30.append((idClient, clientiDupaNrInchirieri[idClient]))
        return clientiOrdonati30

