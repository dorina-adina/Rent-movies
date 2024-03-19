from repository.repository import Repository
from service.ClientService import ClientService



def testAdaugaClientService():
    clientRepository = Repository()
    clientFilmRpository = Repository()
    clientService = ClientService(clientRepository, clientFilmRpository)
    clientService.adauga("1", "Popescu Maria", "6070917234")

    clienti = clientService.getAllClienti()
    assert len(clienti) == 1
    assert clienti[0].getIdEntitate() == "1"

def testModificaClientService():
    clientRepository = Repository()
    clientFilmRpository = Repository()
    clientService = ClientService(clientRepository, clientFilmRpository)
    clientService.adauga("1", "Popescu Maria", "6070917234")

    clientService.modifica("1", "Pop Ioana", "6070917354")

    clienti = clientService.getAllClienti()
    assert clienti[0].getNume() == "Pop Ioana"


def testStergeClientService():
    clientRepository = Repository()
    clientFilmRpository = Repository()
    clientService = ClientService(clientRepository, clientFilmRpository)
    clientService.adauga("1", "Popa Elena", "6070917234")
    clientService.adauga("2", "Popescu Elena", "6072217234")

    clientService.sterge("1")

    clienti = clientService.getAllClienti()
    assert clienti[0].getNume() == "Popescu Elena"



def testOrdoneazaClientiDupaNume():
    clientRepository = Repository()
    clientFilmRpository = Repository()
    clientService = ClientService(clientRepository, clientFilmRpository)
    clientService.adauga("1", "Popa Elena", "6070917234")

    clientService.adauga("2", "Barbu Mara", "6090000000")

    clientService.ordoneazaClientiDupaNume()

    clienti = clientService.getAllClienti()
    assert clienti[1].getNume() == "Barbu Mara"



