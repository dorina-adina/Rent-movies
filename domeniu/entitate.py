from dataclasses import dataclass


@dataclass
class Entitate:
    idEntitate: str

    def getIdEntitate(self):
        return self.idEntitate

    def setIdEntitate(self, other):
        self.idEntitate = other

'''
class Entitate:
    def __init__(self, idEntitate):
        self.__idEntitate = idEntitate

    def getIdEntitate(self):
        return self.__idEntitate

    def setIdEntitate(self, idEntitate):
        self.__idEntitate = idEntitate
'''