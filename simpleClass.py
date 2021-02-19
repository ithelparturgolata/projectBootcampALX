# class A:
#
#     def __init__(self, imie):
#         self.imie = imie
#
# class B(A) :
#
#     def __init__(self, login, imie):
#         super().__init__(imie)
#         self.login = login
#
#
#
# ob = B("rob", "robert")
# print(ob.imie, ob.login)
class Produkt:

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

class Oprogramowanie(Produkt):

    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system

class Szkolenia(Oprogramowanie):

    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin

    def __str__(self):
        return f"{self.nazwa} {self.cena} {self.jezyk} {self.system} {self.termin}"

ob = Szkolenia("Szkolenie Python", 1000, "Python", "Windows", "2020-02-02")
print(ob)
