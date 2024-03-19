from domeniu.film import Film


def testFilm():
    film = Film("1", "Pe aripile vantului", "film bun", "drama")

    assert film.getIdEntitate() == "1"
    assert film.getTitlu() == "Pe aripile vantului"
    assert film.getDescriere() == "film bun"
    assert film.getGen() == "drama"

def testFilmSetteri():
    film = Film("1" ,"Pe aripile vantului", "film bun", "drama")

    film.setIdEntitate("2")
    assert film.getIdEntitate() == "2"

    film.setTitlu("Downfall")
    assert film.getTitlu() == "Downfall"

    film.setDescriere("film la fel de bun")
    assert film.getDescriere() == "film la fel de bun"

    film.setGen("istoric")
    assert film.getGen() == "istoric"


