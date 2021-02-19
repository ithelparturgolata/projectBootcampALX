# class Zawodnik:
#     def __init__(self, imie, wzrost, waga):
#         self.imie = imie
#         self.wzrost = wzrost
#         self.waga = waga
#
#     def obliczBMI(self):
#         wynik = self.waga / (self.wzrost * self.wzrost)
#         print(f" {self.imie} Twoje BMI wynosi: {wynik}")
#
#
# ludzik1 = Zawodnik("Artur", 1.90, 92)
# ludzik2 = Zawodnik("Marcin", 1.80, 80)
#
# ludzik1.obliczBMI()
# ludzik2.obliczBMI()

# listaPracownikow = []
# class Pracownik:
#
#     def __init__(self, imie, nazwisko, email, telefon):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.email = email
#         self.telefon = telefon
#
#     def wyswietlPracownik(self):
#         print(f"{self.imie} {self.nazwisko} {self.email} {self.telefon}")
#
#     def __str__(self):
#         return (f"{self.imie} {self.nazwisko} {self.email} {self.telefon}")
#
#
# for i in range(3):
#     imie = input("Podaj imie: ")
#     nazwisko = input("Podaj nazwisko: ")
#     email = input("Podaj email: ")
#     telefon = input("Podaj telefon: ")
#     pracownik = Pracownik(imie, nazwisko, email, telefon)
#
#     listaPracownikow.append(pracownik)
#
# for i in listaPracownikow:
#     i.wyswietlPracownik()

# while:
#     imie = input("Podaj imie: ")
#     nazwisko = input("Podaj nazwisko: ")
#     email = input("Podaj email: ")
#     telefon = input("Podaj telefon: ")
#     pracownik = Pracownik(imie, nazwisko, email, telefon)
#
#     listaPracownikow.append(pracownik)
#
# for i in listaPracownikow:
#     i.wyswietlPracownik()
