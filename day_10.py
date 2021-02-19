# def funkcjaTestowa(liczb1, liczb2):
#     if liczb1 > liczb2:
#         print(f"Liczba {liczb1} jest większa od {liczb2}")
#     else:
#         print("Nie jest")
#
# funkcjaTestowa(5,8)
# import random
# def licz(lista):
#     najmniejsza = None
#     najwieksza = None
#     for i in lista:
#         if najmniejsza == None or najmniejsza > i:
#             najmniejsza = i
#         if najwieksza == None or najwieksza < i:
#             najwieksza = i
#     print(f"najmniejsza liczba to:", {najmniejsza})
#     print(f"największa liczba to:", {najwieksza})
#
#     suma = sum(lista)
#     srednia = suma / len(lista)
#
#     for y in lista:
#         if y % 2 == 0:
#
#             print(y)
#
# lista = []
# for x in range(10):
#     losowaLiczba = random.randint(1, 100)
#     lista.append(losowaLiczba)
# print("####")
# print(lista)
# licz(lista)
# import random
#
# def licz(listaX, listaY):
#     for i in listaX:
#         if i in listaY:
#             print(i)
# # tutaj defincja normalnego programu
# listaX = []
# listaY = []
# for x in range(10):
#     losowaLiczba1 = random.randint(1, 100)
#     listaX.append(losowaLiczba1)
# for y in range(10):
#     losowaLiczba2 = random.randint(1, 100)
#     listaY.append(losowaLiczba2)
# print(listaX,listaY)
#
# #a tu wywołanie funkcji
# licz(listaX, listaY)

import random
def licz(listaX, listaY):
    pass


# tutaj defincja normalnego programu
listaX = []
listaY = []
maxX = listaX.sort()
maxY = listaY.sort()
for x in range(10):
    losowaLiczba1 = random.randint(1, 30)
    listaX.append(losowaLiczba1)
for y in range(10):
    losowaLiczba2 = random.randint(1, 30)
    listaY.append(losowaLiczba2)
print(listaX,listaY)
print(maxX, maxY)

#a tu wywołanie funkcji
licz(listaX, listaY)