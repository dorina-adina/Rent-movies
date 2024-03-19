from dataclasses import dataclass


@dataclass
class ClientSortareDTO:
    nume : str
    nrFilme : int


@dataclass()
class FilmSortareDTO:
    nume : str
    nrInchirieri : int


class ClientSortareDTOAssembler:
    @staticmethod
    def create_client_dto(client, inchirieri):
        nume = client.getNume()
        nrFilme = 0
        for inchiriere in inchirieri:
            if client.getIdEntitate() == inchiriere.getIdClient():
                nrFilme += 1

        return ClientSortareDTO(nume, nrFilme)


class FilmSortareDTOAssembler:
    @staticmethod
    def create_film_dto(film, inchirieri):
        nume = film.getTitlu()  # Use getNume() method to access the name of the film
        nrInchirieri = 0
        for inchiriere in inchirieri:
            if film.getIdEntitate() == inchiriere.getIdFilm():
                nrInchirieri += 1

        return FilmSortareDTO(nume, nrInchirieri)

