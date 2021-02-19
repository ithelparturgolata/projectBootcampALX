# while(True):
#     try:
#         liczba1 = int(input("Podaj liczbe 1: "))
#         liczba2 = int(input("Podaj liczbe 2: "))
#
#         wynik = liczba1 / liczba2
#         print(wynik)
#     except ZeroDivisionError:
#         print("Nie dzielimy przez 0!")
#     except ValueError:
#         print("Podaj liczbe !!!")

# while(True):
#     try:
#         liczba1 = int(input("Podaj liczbe 1: "))
#         liczba2 = int(input("Podaj liczbe 2: "))
#         charznak = input("Podaj znak działania (+, -, *, / : ")
#         listaZnakow = ["+", "-", "*", "/"]
#         for i in listaZnakow:
#             if i == "+":
#                 wynik = liczba1 + liczba2
#                 print(wynik)
#
#         for i in listaZnakow:
#             if i == "-":
#                 wynik = liczba1 - liczba2
#                 print(wynik)
#
#         for i in listaZnakow:
#             if i == "*":
#                 wynik = liczba1 * liczba2
#                 print(wynik)
#
#         if charznak == "/":
#             if i == "/":
#                 wynik = liczba1 / liczba2
#                 print(wynik)
#     except ZeroDivisionError:
#         print("Nie dzielimy przez 0!")
#     except ValueError:
#         print("Podaj liczbe !!!")
