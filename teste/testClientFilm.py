from domeniu.clientFilm import ClientFilm


def testClientFilm():
    clientFilm = ClientFilm("99", "1", "5")

    assert clientFilm.getIdClient() == "1"
    assert clientFilm.getIdFilm() == "5"


def testClientFilmSetteri():
    clientFilm = ClientFilm("98", "2", "6")


    clientFilm.setIdClient("2")
    assert clientFilm.getIdClient() == "2"

    clientFilm.setIdFilm("6")
    assert clientFilm.getIdFilm() == "6"






