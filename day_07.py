# import random
# liczba1 = random.randint(1, 9)
# liczba2 = random.randint(1,9)
# print(liczba1, liczba2)
# znakDzialania = random.randint(1,3)
#
# if (znakDzialania == 1):
#     wynikU = int(input(f"Ile to jest {liczba1} + {liczba2} ?: "))
#     wynikK = liczba1+liczba2
# elif (znakDzialania == 2):
#     wynikU = int(input(f"Ile to jest {liczba1} - {liczba2} ?: "))
#     wynikK = liczba1 - liczba2
# elif (znakDzialania == 3):
#     wynikU = int(input(f"Ile to jest {liczba1} * {liczba2} ?: "))
#     wynikK = liczba1 * liczba2
# if (wynikU == wynikK):
#     print("Jest ok")
# else:
#     print("Zle")
# zmiennaWzrost = int(input("Podaj wzrost : "))
# listaWzrost = [0, 165, 175]
# if (zmiennaWzrost > listaWzrost[0] and zmiennaWzrost < listaWzrost [1]):
#     print("niski wzrost")
# elif (zmiennaWzrost > listaWzrost[1] and zmiennaWzrost < listaWzrost [2]):
#     print("średni wzrost")
# elif (zmiennaWzrost > listaWzrost[2]):
#     print("wysoki wzrost")
# liczX = int(input("podaj liczbe x: "))
# liczY = int(input("podaj liczbe y: "))
# if liczX > liczY:
#     print("X jest wiekszy od Y:")
#     if liczX *2 > liczY:
#         print("Tak jest wiekszy.")
#     else:
#         print("Nie jest wiekszy.")
# elif liczY < liczX + 3 and liczY > liczX -2:
#     print("Tak jest")
# else:
#     print("Nie jest")
# if (liczX * liczY) % 2 == 0:
#     print("liczby sa parzyste")
# else:
#     print("nie są parzyste.")
# for i in range(1, 101):
#     if (i % 7 == 0):
#         print(i)
# listaImion = []
# for i in range(10):
#     imie = input("Podaj imie: ")
#     listaImion.append(imie)
# for imie in listaImion:
#     print(f"Cześć {imie}")
# listaLiczb = []
# suma = 0
# for i in range (15):
#     liczba = int(input("Podaj liczbe: "))
#     if (liczba % 2 == 0):
#         suma = suma + liczba
# print(suma)
# podstawa = int(input("Podaj podstawe: ")) #2
# wykladnik = int(input("Podaj wykladnik: ")) #3
#
# wynik = 0
# for i in range(wykladnik-1):
#
#     if (i == 0):
#         wynik = podstawa * podstawa
#     else:
#         wynik = podstawa * wynik
#
# print(wynik)
