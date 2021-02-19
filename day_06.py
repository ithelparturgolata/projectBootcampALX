# liczba = int(input("Podaj liczbę: "))
# if (liczba % 2 == 0):
#     print("liczba parzysta")
# else:
#     print("liczba nieparzysta")
# liczba1 = int(input("Podaj wartos liczby 1: "))
# liczba2 = int(input("Podaj wartos liczby 2: "))
# liczba3 = int(input("Podaj wartos liczby 3: "))
#
# if (liczba1 > liczba2 and liczba1 > liczba3):
#     print(liczba1)
# elif (liczba2 > liczba3):
#     print(liczba2)
# else:
#     print(liczba3)
# a = int(input("Podaj pierwszą liczbę:"))
# b = int(input("Podaj drugą liczbę:"))
# c = int(input("Podaj trzecią liczbę:"))
# if (a > b > c):
#     print("Największa liczba:", a)
# if (a < b > c):
#     print("Największa liczba:", b)
# else:
#     print("Największa liczba:", c)
# numbers = [a, b, c]
# numbers.sort()
# print(numbers[0], numbers[1], numbers[2], sep=", ")
# a = int(input("Liczba 1")) # 10
# b = int(input("Liczba 2")) # 5
# c = int(input("Liczba 3")) # 9
#
# if(a < b and a < c):
#     if (b < c):
#         print(a, b, c)
#     else:
#         print(a, c, b)
#
# elif(b < a and b < c):
#     if(a < c):
#         print(b, a, c)
#     else:
#         print(b, c, a)
#
# elif(c < a and c < b):
#     if(a < b):
#         print(c, a, b)
#     else:
#         print(c, b, a)
a = int(input("Liczba 1"))
b = int(input("Liczba 2"))
c = int(input("Liczba 3"))

min = a
max = a

if (max < b):
    max = b

if (min > b):
    min = b

if (max < c):
    max = c

if (min > c):
    min = c

print(f"Min to {min} Max to {max}")


