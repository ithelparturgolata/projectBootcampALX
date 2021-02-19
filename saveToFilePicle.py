import pickle

class Kontakt:
    def __init__(self, imie, nazwisko, noweImie, noweNazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__telefony = []
        self.__email = []
        self.__noweImie = noweImie
        self.__noweNazwisko = noweNazwisko

    def getImie(self):
        return self.__imie

    def setImie(self, imie):
        self.__imie = imie

    def getNazwisko(self):
        return self.__nazwisko

    def setNazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def getnoweImie(self):
        return self.__noweImie

    def setnoweImie(self, noweImie):
        self.__noweImie = noweImie

    def getnoweNazwisko(self):
        return self.__noweNazwisko

    def setnoweNazwisko(self, noweNazwisko):
        self.__noweNazwisko = noweNazwisko

    def getTelefon(self):
        return self.__telefony

    def setTelefon(self, telefon):
        self.__telefony = telefon

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def __str__(self):
        # return "Imię: " + self.__imie + " Nazwisko: " + self.__nazwisko + " Telefon:" + str(self.__telefony)
        return (f"Imię: {self.__imie} Nazwisko: {self.__nazwisko} Telefon: {self.__telefony} Email: {self.__email}")

class KontaktController:

    def __init__(self):
        self.kontakty = []

    def dodajKontakt(self, imie, nazwisko):
        obj = Kontakt(imie, nazwisko)
        self.kontakty.append(obj)
        f = open("86_3.dat", "wb")
        pickle.dump(self.kontakty, f)
        f.close()
        print("Dodano kontakt")

    def dodajTelefon(self, nazwisko, telefon):
        znaleziono = False
        for i in (self.kontakty):
            if i.getNazwisko() == nazwisko:
                i.setTelefon(telefon)
                znaleziono = True
                break
                # zapisanie listy do pliku
        if (znaleziono == True):
            f = open("86_3.dat", "wb")
            pickle.dump(self.kontakty, f)
            f.close()
            print("Dodano telefon")
        else:
            print('Nie ma takiej osoby')

    def dodajEmail(self, nazwisko, email):
        znaleziono = False
        for i, v in enumerate(self.kontakty):
            if v.getNazwisko() == nazwisko:
                v.setEmail(email)
                znaleziono = True
                break
                # zapisanie listy do pliku
        if (znaleziono == True):
            f = open("86_3.dat", "wb")
            pickle.dump(self.kontakty, f)
            f.close()
            print("Dodano email")
        else:
            print('Nie ma takiej osoby')

    def usunKontakt(self, nazwisko):
        znaleziono = False
        for i, v in enumerate(self.kontakty):
            if v.getNazwisko() == nazwisko:
                self.kontakty.pop(i)
                znaleziono = True
                break
                # zapisanie listy do pliku
        if (znaleziono == True):
            f = open("86_3.dat", "wb")
            pickle.dump(self.kontakty, f)
            f.close()
            print("Kontakt został usunięty")
        else:
            print('Nie ma takiej osoby')

    def usunTelefon(self, nazwisko):
        znaleziono = False
        for i in (self.kontakty):
            if i.getNazwisko == nazwisko:
                i.setTelefon(" ")
                znaleziono = True
                break
        if (znaleziono == True):
            f = open("86_3.dat", "wb")
            pickle.dump(self.kontakty, f)
            f.close()
            print("Telefon został usunięty")
        else:
            print("Nie ma takiej osoby")

    def modyfikujKontakt(self, nazwisko, noweNazwisko, noweImie):
        znaleziono = False
        for i, v in enumerate(self.kontakty):
            if v.getNazwisko() == nazwisko:
                v.setImie(noweImie)
                v.setNazwisko(noweNazwisko)
                znaleziono = True
                break
                # zapisanie listy do pliku
        if (znaleziono == True):
            f = open("86_3.dat", "wb")
            pickle.dump(self.kontakty, f)
            f.close()
            print("Kontakt został zmodyfikowany")
        else:
            print('Kontakt zmieniono')

    def pokazKontaky(self):
        for i in self.kontakty:
            print(i)

class App(KontaktController):

    def __init__(self):
        super().__init__()
        try:
            f = open("86_3.dat", "rb")
            self.kontakty = pickle.load(f)
            f.close()
        except:
            f = open("86_3.dat", "wb")
            pickle.dump([], f)
            f.close()
        self.menu()

    def menu(self):
        global telefon
        while(True):

                menu = int(input("1 - pokaz kontakt\n "
                    "2 - dodaj kontakt\n "
                    "3 - dodaj telefon\n "
                    "4 - dodaj email\n "
                    "5 - usun kontakt\n "
                    "6 - usun telefon\n "
                    "7 - modyfikuj kontakt\n "
                    "8 - koniec\n"
                    "Wybierz: "))

                if (menu == 1):
                    self.pokazKontaky()

                elif (menu == 2):
                    imie = input("Podaj imię : ")
                    nazwisko = input("Podaj nazwisko : ")
                    self.dodajKontakt(imie, nazwisko)

                elif (menu == 3):
                    nazwisko = input("Podaj komu chcesz dodać numer: ")
                    telefon = input("Podaj nr telefonu: ")
                    self.dodajTelefon(nazwisko, telefon)

                elif (menu == 4):
                    nazwisko = input("Podaj komu chcesz dodać email: ")
                    email = input("Podaj email: ")
                    self.dodajEmail(nazwisko, email)

                elif (menu == 5):
                    nazwisko = input("Podaj nazwisko  do usunięcia: ")
                    self.usunKontakt(nazwisko)

                elif (menu == 6):
                    nazwisko = input("Podaj nazwisko: ")
                    self.usunTelefon(nazwisko)

                elif (menu == 7):
                    nazwisko = input("Podaj nazwisko : ")
                    noweNazwisko = input("Podaj nowe nazwisko: ")
                    noweImie = input("Podaj nowe imię: ")
                    self.modyfikujKontakt(nazwisko, noweNazwisko, noweImie)

                elif (menu == 8):
                    f = open("86_3.dat", "wb")
                    pickle.dump(self.kontakty, f)
                    f.close()
                    print("Koniec")
                    break
                else:
                    print("Nierozpoznana opcja menu. Wybierz od 1 do 7")
app = App()

# import pickle
# #
# # print("Marynowanie list i obiektu")
# #
# # smak = ["łagodny", "pikantny"]
# # firma = ["dawtona", "pudliszki"]
# #
# # f = open("dane.dat", "wb")
# # pickle.dump(smak, f)
# # pickle.dump(firma, f)
# # f.close()
#
# import pickle
#
# print("Marynowanie list i obiektu.")
#
# smak = ["łagodny", "pikantny", "kwaszony"]
# firma = ["Dawtona", "Klimex", "Vortumnus"]
#
# f = open("dane.dat", "wb")
# pickle.dump(smak, f)
# pickle.dump(firma, f)
# f.close()
#
# print("Odmarynowanie list i obiektu.")
# f = open("dane.dat", "rb")
# smak = pickle.load(f)
# firma = pickle.load(f)
#
# print(type(smak))
# print(firma)
# f.close()
# import pickle
#
# print("Marynowanie list i obiektu.")
#
# class Auto:
#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model
#
#     def hello(self):
#         print("hello")
#
#     def __str__(self):
#         return self.marka+" "+self.model
#
# obj = Auto("VW", "PASSAT")
#
# f = open("dane.dat", "wb")
# pickle.dump(obj, f)
# f.close()
#
# print("Odmarynowanie list i obiektu.")
# f = open("dane.dat", "rb")
# abc = pickle.load(f)
#
# print(abc)
# abc.hello()
#
# f.close()


# def odczyt(self):
#     try:
#         f = open("86_3.dat", "rb")
#         self.kontakty = pickle.load(f)
#         f.close()
#     except:
#         f = open("86_3.dat", "wb")
#         pickle.dump([], f)
#         f.close()
#
# def zapis(self):
#     f = open("86_3.dat", "wb")
#     pickle.dump(self.kontakty, f)
#     f.close()
