#pomysły na zadania zaczerpnięte ze strony:
#https://programeria.pl/2017/05/25/proste-projekty-dla-poczatkujacych/

#PALINDROMY działa tylko dla pojedynczych wyrazów
# wyraz = input("Podaj wyraz do sprawdzenia: ")
# print(f"Wyraz podany to : ",wyraz)
# czyPalindrom = wyraz[::-1]
# if wyraz == czyPalindrom:
#     print(czyPalindrom + " : " + "Ten wyraz jest palindromem.")
# else:
#     print(wyraz + " : " + "Ten wyraz nie jest palindromem.")

#ZGADYWANIE LICZB
# import random
# liczbaA = int(input("Podaj liczbę od 1 do 100: "))
# liczbaB = random.randint(1, 100)
# print(f"Dla poprawności działania drukuję podaną i wylosowaną liczbę: ", liczbaA, liczbaB)
# if liczbaA == liczbaB:
#     print("Brawo trafiłeś.")
# elif liczbaA > liczbaB:
#     print("Podałeś za dużą liczbę od wylosowanej.")
# else:
#     print("Podałeś za małą liczbę.")

#PRZELICZANIE TEMPERATUR
# print("Kalkultor Celsjuszy na Fahrenheita")
# stopienF = float(input("Podaj ile stopni F: "))
# wynikF = (stopienF - 32) * (5 / 9)
# f = round(wynikF,2)
# print(f"Po przeliczeniu otrzymujemy stopni Celsjusza: {f}")
# print("####" * 3)
# print("Kalkultor Fahrenheit'a na Celsjusza")
# stopienC = float(input("Podaj ile stopni C: "))
# wynikC = (stopienC * 9 / 5) + 32
# c = round(wynikC,2)
# print(f"Po przeliczeniu otrzymujemy stopni Fahrenheita: {c}")

#FIZZBUZZ CZYLI BOLEK LOLEK TOLA :)
import random
for liczba in range(1, 100):
    if (liczba % 3 == 0 and liczba % 5 == 0):
        print(f"Bolek Lolek, {liczba}")
    elif (liczba % 5 == 0):
        print("Bolek")
    elif (liczba % 3 == 0):
        print("Lolek")
    else:
        print("Tola")


