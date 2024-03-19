from domeniu.exceptii.duplicateError import DuplicateError


class Repository:
    def __init__(self):
        self._entitati = {}

    def getAll(self):
        '''
        returneaza lista de clienti
        :return: o lista de obiecte de tipul Client
        '''
        return list(self._entitati.values())

    def getById(self, idEntitate):
        '''
        returneaza clientul cu id-ul dat
        :param idEntitate: entitate
        :return: un obiect de tipul Client, daca exista unul cu id-ul dat, altfel None
        '''

        if idEntitate in self._entitati:
            return self._entitati[idEntitate]
        return None

    def adauga(self, entitate):
        '''
        adauga un client in dictionar
        :param entitate: obiect de tipul Client
        :return:
        '''
        if self.getById(entitate.getIdEntitate()) is not None:
            raise DuplicateError("Exista deja o entitate cu id-ul dat!")
        self._entitati[entitate.getIdEntitate()] = entitate

    def modifica(self, entitateNoua):
        '''
        modifica un client dupa id
        :param entitateNoua: obiect de tipul Client
        :return:
        '''
        if self.getById(entitateNoua.getIdEntitate()) is None:
            raise KeyError("Nu exista o entitate cu acest id!")
        self._entitati[entitateNoua.getIdEntitate()] = entitateNoua

    def sterge(self, idEntitate):
        '''
        sterge un client dupa id
        :param idEntitate: string
        :return:
        '''

        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista o entitate cu id-ul dat!")
        self._entitati.pop(idEntitate)