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

    def adaugaClientUI(self):
        try:
            idClient = input("Dati id-ul clientului: ")
            nume = input("Dati numele clientului: ")
            cnp = input("Dati cnp-ul clientului: ")
            self.__clientService.adauga(idClient,nume,cnp)
        except DuplicateError as e:
           print(e)
        except ValueError as e :
            print(e)

    def modificaClientUI(self):
        try:
            idClient = input("Dati id-ul clientului de modificat: ")
            numeNou = input("Dati numele nou al clientului: ")
            cnpNou = input("Dati CNP-ul nou al clientului: ")
            self.__clientService.modifica(idClient, numeNou, cnpNou)
            print()
        except KeyError as e :
            print(e)
        except ValueError as e:
            print(e)


    def stergeClientUI(self):
        try:
            idClient = input("Dati id-ul client de sters: ")
            self.__clientService.sterge(idClient)
        except KeyError as e :
            print(e)
        except ValueError as e:
            print(e)

    def adaugaFilmUI(self):
        try:
            idFilm = input("Dati id-ul filmului: ")
            titlu = input("Dati titlul filmului: ")
            descriere = input("Dati descrierea filmului: ")
            gen = input("Dati genul  filmului: ")
            self.__filmService.adaugaFilm(idFilm, titlu, descriere, gen)
        except ValueError as e:
            print(e)

    def modificaFilmUI(self):
        try:
            idFilm = input("Dati id-ul filmului de modificat: ")
            titluNou = input("Dati noul titlu al filmului: ")
            descriereNoua = input("Dati noua descriere a filmului: ")
            genNou = input("Dati noul gen al filmului: ")
            self.__filmService.modificaFilm(idFilm, titluNou, descriereNoua, genNou)
        except KeyError as e:
            print(e)

    def stergeFilmUI(self):
      try:
            idFilmSters = input("Dati id-ul filmului de sters: ")
            self.__filmService.stergeFilm(idFilmSters)
      except KeyError as e:
           print(e)
      except ValueError as e:
           print(e)


    def inchiriazaFilmLaClientUI(self):
        try:
            idClientFilm = input("Dati id-ul inchirierii: ")
            idClient = input("Dati id-ul clientului: ")
            idFilm = input("Dati id-ul filmului: ")
            self.__clientFilmService.adaugaInchiriere(idClientFilm, idClient, idFilm)
        except KeyError as e:
            print(e)

    def stergeLegaturaFilmLaClientUI(self):
        idClient = input("Dati id-ul clientului: ")
        idFilm = input("Dati id-ul filmului: ")
        self.__clientFilmService.stergeInchiriere(idClient, idFilm)

    def ordoneazaClientiAlfabetic(self):
        rezultat = self.__clientFilmService.ordoneazaClientiDupaNume()
        self.afiseazaEntitati(rezultat)

    def ordoneazaClientiDupaFilme(self):
        rezultat = self.__clientFilmService.ordoneazaClientiDupaNrFilme()
        self.afiseazaEntitati(rezultat)

    def ordoneazaClientiDupaFilme30(self):
        rezultat = self.__clientFilmService.ordoneazaClientiDupaNrFilme30()
        self.afiseazaEntitati(rezultat)


    def ordoneazaFilmeDupaInchirieriUI(self):
        rezultat = self.__clientFilmService.ordoneazaFilmeDupaNrInchirieri()
        self.afiseazaEntitati(rezultat)

    def afiseazaEntitati(self, entitati):
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
        print("9. Clienti cu filme inchiriate ordonati dupa numarul de inchirieri")
        print("10. Filme inchiriate ordonate dupa numarul de inchirieri")
        print("11. Primii 30% clienti cu cele mai multe filme")
        print("12. 3 cele mai inchiriate filme")
        print("a. Afiseaza toti clientii")
        print("t. Afiseaza toate filmele")
        print("i. Afiseaza toate inchirierile")
        print("x. Iesire")


    def meniu(self):
        while True :
            self.printMeniu()
            optiune = input("Introduceti optiunea: ")
            if optiune == "1":
                self.adaugaClientUI()
            elif optiune == "2":
                self.modificaClientUI()
            elif optiune == "3":
                self.stergeClientUI()
            elif optiune == "4":
                self.adaugaFilmUI()
            elif optiune == "5":
                self.modificaFilmUI()
            elif optiune == "6":
                self.stergeFilmUI()
            elif optiune == "7":
                self.inchiriazaFilmLaClientUI()
            elif optiune == "8":
                self.stergeLegaturaFilmLaClientUI()
            elif optiune == "9":
                self.afiseazaEntitati(self.__clientFilmService.sotrareClientiDupaNrDeFilmeInchiriate())
            elif optiune == "10":
                self.afiseazaEntitati(self.__clientFilmService.sortareFilmeDupaNrDeInchirieri())
            elif optiune == "11":
                self.afiseazaEntitati((self.__clientFilmService.get30Filme()))
            elif optiune == "12":
                self.ordoneazaFilmeDupaInchirieriUI()
            elif optiune == "a":
                self.afiseazaEntitati(self.__clientService.getAllClienti())
            elif optiune == "t":
                self.afiseazaEntitati(self.__filmService.getAllFilme())
            elif optiune == "i":
                self.afiseazaEntitati((self.__clientFilmService.getAllInchirieri()))
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reincercati!")