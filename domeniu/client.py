from domeniu.entitate import Entitate

class Client(Entitate):
    def __init__(self, idClient, nume, cnp):

        super().__init__(idClient)
        self.__nume = nume
        self.__cnp = cnp

    def getNume(self):
        return self.__nume

    def getCNP(self):
        return self.__cnp

    def setNume(self, nume):
        self.__nume = nume

    def setCNP(self, cnp):
        self.__cnp = cnp


    def __str__(self):
        return f"id: {self.getIdEntitate()}, nume: {self.__nume}, CNP: {self.__cnp}"
