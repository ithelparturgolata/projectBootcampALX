class Student:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodajOcene(self, ocena):
        if ocena in range(2,6):#dodałem zakres ale na intach wszystko, wiadomo ocen typu 6 i wyżej lub 1 na studiach nie ma
            self.oceny.append(ocena)
        else:
            print("Ocena musi być z zakresu 2 - 5")

    def wypiszOceny(self):
        if self.oceny == []:#tutaj dorobiłem, jeśli mamy brak ocen pojawi się stosowny komunikat
            print("Brak ocen.")
        else:
            for i in self.oceny:
                print(i)

    def policzSrednia(self):
        suma = 0
        for i in self.oceny:
            suma += i
        if suma == 0:#jeżeli nie ma ocen czyli jest 0 a wiadomo jak z dzieleniem to dajemy komunikat, że brak ocen
            print("Brak ocen by wyświetlić średnią.")
        elif suma != 0:
            srednia = suma / len(self.oceny)
            print(f"Srednia studenta to: {srednia}")

    def usunStudenta(self):
        if obj.nazwisko in listaStudentow:
            listaStudentow.remove(obj.nazwisko)

    def edycjaStudenta(self, imie, nazwisko, noweImie, noweNazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.noweImie = noweImie
        self.noweNazwisko = noweNazwisko

    def __str__(self):
        return f"Imie: {self.imie} Nazwisko: {self.nazwisko}"

def wybor():
    print("Menu:")
    print("[1] - Dodaj studenta")
    print("[2] - Lista studentów")
    print("[3] - Dodaj ocenę")
    print("[4] - Wypisz oceny")
    print("[5] - Średnia studenta")
    print("[6] - Usuń studenta")
    print("[7] - Edycja studenta")
    print("[8] - Koniec programu")

def wyborNazwisko():
    nazwisko = input("Podaj nazwisko do edycji: ")

listaStudentow = []

while(True):

    wybor()
    try:
        option = int(input("Wybierz: "))

        while option !=0:
            if option == 1:
                imie = input("Podaj imię: ")
                nazwisko = input("Podaj nazwisko: ")
                student = Student(imie, nazwisko)
                listaStudentow.append(student)

            elif option == 2:
                for i in listaStudentow:
                    print(i)
                    print("XXX"*10)

            elif option == 3:
                nazwisko = input("Podaj nazwisko: ")
                znaleziono = False
                for obj in listaStudentow:
                    if (obj.nazwisko == nazwisko):
                        ocena = int(input("Podaj ocenę: "))
                        obj.dodajOcene(ocena)
                        znaleziono = True
                        break
                if (znaleziono == False):
                        print(f"Student o nazwisku: {nazwisko} nie istnieje.")

            elif option == 4:
                nazwisko = input("Podaj nazwisko: ")
                znaleziono = False
                for obj in listaStudentow:
                    if (obj.nazwisko == nazwisko):
                        obj.wypiszOceny()
                        znaleziono = True
                        break
                if (znaleziono == False):
                    print(f"Student o nazwisku: {nazwisko} nie istnieje.")

            elif option == 5:
                nazwisko = input("Podaj nazwisko: ")
                znaleziono = False
                for obj in listaStudentow:
                    if (obj.nazwisko == nazwisko):
                        obj.policzSrednia()
                        znaleziono = True
                        break
                if (znaleziono == False):
                    print(f"Student o nazwisku: {nazwisko} nie istnieje.")

            elif option == 6:
                nazwisko = input("Podaj nazwisko: ")
                znaleziono = False
                for obj in listaStudentow:
                    if obj.nazwisko == nazwisko:
                        listaStudentow.remove(obj)
                        znaleziono = True
                        print(f"Pomyślnie usunięto studenta: {nazwisko}.")
                        continue
                if (znaleziono == False):
                    print(f"Student o nazwisku: {nazwisko} nie istnieje.")

            elif option == 7:
                nazwisko = input("Podaj nazwisko do edycji: ")
                znaleziono = False
                for obj in listaStudentow:
                    if (obj.nazwisko == nazwisko):
                        noweNazwisko = input("Podaj nowe nazwisko: ")
                        noweImie = input("Podaj nowe imię: ")
                        student = Student(noweNazwisko, noweImie)

                        znaleziono = True
                        break
                if (znaleziono == False):
                    print(f"Student o nazwisku: {nazwisko} nie istnieje.")

            elif option == 8:
                print("koniec programu")
                break
            else:
                print("Wybrałeś złą opcję.")
            wybor()
            option = int(input("Wybierz:"))
    except ValueError:
        print("Musisz podać liczbę !!!")

