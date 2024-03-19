from teste.testClient import testClient, testClientSetteri
from teste.testClientFilm import testClientFilm, testClientFilmSetteri
from teste.testRepository import testAdaugaRepository, testModificaRepository, testStergeRepository
from teste.testClientService import testAdaugaClientService, testModificaClientService, testOrdoneazaClientiDupaNume
from teste.testEntitate import testEntitate, testEntitateSetteri
from teste.testFilm import testFilm, testFilmSetteri
from teste.testFilmService import testAdaugaFilmSevice, testModificaFilmService
from teste.unire import test_str_clientfilm, test_str_film, test_str_client


def testAll():
    testClient()
    testClientSetteri()
    test_str_client()

    testFilm()
    testFilmSetteri()
    test_str_film()

    testClientFilm()
    testClientFilmSetteri()
    test_str_clientfilm()

    testEntitate()
    testEntitateSetteri()

    testAdaugaRepository()
    testModificaRepository()
    testStergeRepository()

    #testAdaugaFilmRepository()
    #testModificaFilmRepository()
    #testStergeFilmRepository()

    testAdaugaClientService()
    testModificaClientService()
    #testStergeClientService()
    testOrdoneazaClientiDupaNume()

    testAdaugaFilmSevice()
    testModificaFilmService()
    #testStergeFilmService()




