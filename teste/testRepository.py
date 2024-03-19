from domeniu.entitate import Entitate
from domeniu.exceptii.duplicateError import DuplicateError
from repository.repository import Repository


def testAdaugaRepository():
    entitateRepository = Repository()
    entitate = Entitate("1")

    entitateRepository.adauga(entitate)

    entitati = entitateRepository.getAll()
    assert len(entitati) == 1
    assert entitati[0].getIdEntitate() == "1"

    try:
        entitateRepository.adauga(entitate)
    except DuplicateError:
        ...


def testModificaRepository():
    entitateRepository = Repository()
    entitate = Entitate("1")
    entitateNoua = Entitate("1")
    entitateNoua2 = Entitate("66")
    entitateRepository.adauga(entitate)

    entitateRepository.modifica(entitateNoua)

    entitati = entitateRepository.getAll()
    assert entitati[0].getIdEntitate() == "1"

    try:
        entitateRepository.modifica(entitateNoua2)

    except KeyError:
        ...

def testStergeRepository():
    entitateRepository = Repository()
    entitate = Entitate("1")
    entitate1 = Entitate("2")
    entitateRepository.adauga(entitate)

    entitateRepository.sterge("1")

    assert len(entitateRepository.getAll()) == 0

    try:
        entitateRepository.sterge(entitate1)

    except KeyError:
        ...