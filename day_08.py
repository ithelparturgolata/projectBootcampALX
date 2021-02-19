# zbiorLiczb = set ()
# for x in range(10):
#     liczba = int(input("Podaj liczbę: "))
#     zbiorLiczb.add(liczba)
# for value in zbiorLiczb:
#     print(value)
# suma = 0
# ile = 0
#
# while (True):
#     liczby = int(input("Podaj dowolna liczbe (0-koniec)"))
#
#     if (liczby == 0):
#         break
#     else:
#         suma = suma + liczby
#         ile = ile + 1
#
# srednia = suma / ile
# print(srednia)
import random
los = random.randint(1, 10)
licznik = 0

while True:
    licznik += 1
    liczba = int(input("podaj liczbę: "))
    if (liczba > los):
        print("Za dużo")
    elif (liczba < los):
        print("Za mało")
    elif (liczba == los):
        print("Gratulacje trafiłeś")
        break
    if licznik > 5:
        print("Wykorzytsałes 5 możliwości")
        break
print("Czy chcesz zagrać ponownie T - tak, N - nie")
# if charZnak == "t":
#
# if charZnak == "n":
#     print("Koniec gry.")

