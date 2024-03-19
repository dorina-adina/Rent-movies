# from domeniu.exceptii.ValidationException import ValidationError
from domeniu.exceptii.duplicateError import DuplicateError
from service.ClientService import ClientService
from service.FilmService import FilmService
from service.clientFilmService import ClientFilmService


class Consola:
    def __init__(self, clientService: ClientService,
                 filmService: FilmService,
                 clientFilmService: ClientFilmService):
        self.__clientService = clientService
        self.__filmService = filmService
        self.__clientFilmService = clientFilmService


    def adaugaClient(self):
        try:
            idClient = input("Dati id-ul clientului: ")
            nume = input("Dati numele clientului: ")
            cnp = input("Dati CNP-ul clientului: ")

            self.__clientService.adauga(idClient, nume, cnp)
        except DuplicateError as e:
           print(e)
        except ValueError as e:
            print(e)

    def adaugaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului: ")
            titlu = input("Dati titlul filmului: ")
            descriere = input("Dati descrierea filmului: ")
            gen = input("Dati genul  filmului: ")

            self.__filmService.adaugaFilm(idFilm, titlu, descriere, gen)
        except DuplicateError as e:
           print(e)
        # except ValidationError as e:
        #     print(e)
        except ValueError as e:
            print(e)


    def modificaClient(self):
        try:
            idClient = input("Dati id-ul clientului de modificat: ")
            numeNou = input("Dati numele nou al clientului: ")
            cnp = input("Dati CNP-ul lientului: ")

            self.__clientService.modifica(idClient, numeNou, cnp)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modificaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului de modificat: ")
            titluNou = input("Dati noul titlu al filmului: ")
            descriereNoua = input("Dati noua descriere a filmului: ")
            genNou = input("Dati noul gen al filmului: ")
            self.__filmService.modificaFilm(idFilm, titluNou, descriereNoua, genNou)
        except KeyError as e:
            print(e)
        #except ValidationError as e:
        #    print(e)
        except ValueError as e:
            print(e)


    def stergereClient(self):
        try:
            idClient = input("Dati id-ul clientului de sters: ")
            self.__clientService.sterge(idClient)
        except KeyError as e:
            print(e)

    def stergeFilm(self):
        try:
            idFilm = input("Dati id-ul fimului de sters: ")
            self.__filmService.stergeFilm(idFilm)
        except KeyError as e:
            print(e)

    def inchiriereClientFIlm(self):
        try:
            idClientFilm = input("Dati id-ul inchirierii: ")
            idClient = input("Dati id-ul clientului: ")
            idFilm = input("Dati id-ul filmului: ")
            self.__clientFilmService.adaugaInchiriere(idClientFilm, idClient, idFilm)
        except DuplicateError as e:
           print(e)
        except KeyError as e:
            print(e)

    def stergeInchiriere(self):
        idClient = input("Dati id-ul clientului: ")
        idFilm = input("Dati id-ul filmului: ")
        self.__clientFilmService.stergeInchiriere(idClient, idFilm)


    def ordoneazaClientiAlfabetic(self):
        rezultat = self.__clientFilmService.ordoneazaClientiDupaNume()
        self.afiseaza(rezultat)


    def ordoneazaClientiDupaFilme(self):
        rezultat = self.__clientFilmService.ordoneazaClientiDupaNrFilme()
        self.afiseaza(rezultat)

    def ordoneazaFilmeDupaInchirieri(self):
        rezultat = self.__clientFilmService.ordoneazaFilmeDupaNrInchirieri()
        self.afiseaza(rezultat)

    def ordoneazaClientiDupaFilme30(self):
        rezultat = self.__clientFilmService.ordoneazaClientiDupaNrFilme30()
        self.afiseaza(rezultat)

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def printMeniu(self):
        print("1. Adauga client")
        print("2. Modifica client")
        print("3. Sterge client")
        print("4. Adauga film")
        print("5. Modifica film")
        print("6. Sterge film")
        print("7. Clientul inchiriaza un film")
        print("8. Sterge inchiriere")
        print("9. Ordoneaza clientii dupa numar filme")
        print("10. 3 cele mai inchiriate filme")
        print("11. Primii 30% clienti cu cele mai multe filme")
        print("12. Clientii ordonati alfabetic")
        print("a. Afiseaza toti clientii")
        print("t. Afiseaza toate filmele")
        print("i. Afiseaza toate inchirierile")
        print("x. Iesire")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.adaugaClient()
            elif optiune == "2":
                self.modificaClient()
            elif optiune == "3":
                self.stergereClient()
            elif optiune == "4":
                self.adaugaFilm()
            elif optiune == "5":
                self.modificaFilm()
            elif optiune == "6":
                self.stergeFilm()
            elif optiune == "7":
                self.inchiriereClientFIlm()
            elif optiune == "8":
                self.stergeInchiriere()

            elif optiune == "9":
                self.ordoneazaClientiDupaFilme()
            elif optiune == "10":
                self.ordoneazaFilmeDupaInchirieri()
            elif optiune == "11":
                self.ordoneazaClientiDupaFilme30()
            elif optiune == "12":
                self.ordoneazaClientiAlfabetic()
            elif optiune == "a":
                self.afiseaza(self.__clientService.getAllClienti())
            elif optiune == "t":
                self.afiseaza(self.__filmService.getAllFilme())
            elif optiune == "i":
                self.afiseaza(self.__clientFilmService.getAllInchirieri())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reicercati!")



