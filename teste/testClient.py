from domeniu.client import Client

def testClient():
    client = Client("1", "Popescu Maria", "6070917234")

    assert client.getIdEntitate() == "1"
    assert client.getNume() == "Popescu Maria"
    assert client.getCNP() == "6070917234"

def testClientSetteri():
    client = Client("2", "Popescu Maria", "6070917234")

    client.setIdEntitate("2")
    assert client.getIdEntitate() == "2"

    client.setNume("Popa Paul")
    assert client.getNume() == "Popa Paul"

    client.setCNP("6070917294")
    assert client.getCNP() == "6070917294"


