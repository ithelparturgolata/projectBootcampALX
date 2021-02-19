 # class Osoba:
#
#     def __init__(self, imie):
#         self.imie = imie
#         self.wzrost = 0
#
#     def rosnij(self, ile):
#         self.wzrost += ile
#         return "hello"
#
#     def __str__(self):
#         return (f"{self.imie} {self.wzrost}")
#
#
#
# osoba1 = Osoba("Adam")
# osoba2 = Osoba("Mateusz")
# osoba3 = Osoba("Michal")
#
# print(osoba1.imie)
# print(osoba2)
# print(osoba3)



#klasa Osoba
class Osoba:
#najpierw konstruktor ini na 1 miejscu, definiujemy pola
#to jest argument _imie
    def __init__(self, _imie, _wzrost):
        self.imie = _imie
        self.wzrost = _wzrost
#definijuemy metody na 2 miejscu(funkcje, czynnosci)
    def chodzic(self):
        print("chodze!!!")
#a toString czyli str metode na samym koncu
#tworzymy- budujemy  obiekty na podstawie klasy Osoba
#obiekty sie nie nadpisuja
    def __str__(self):
        return (f"{self.imie} {self.wzrost}")
obj1 = Osoba()
obj2 = Osoba()

obj1.imie = "Tomasz"
obj1.wzrost = 158

obj2.imie = "Anna"
obj2.wzrost = 168

print(obj1.imie, obj1.wzrost)
print(obj2.imie, obj2.wzrost)
