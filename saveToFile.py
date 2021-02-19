# plik = open("84.txt", "w")
# plik.write("Artur\n")
# plik.write("Robert\n")
# plik.close()
#
# plik = open("84.txt", "a")
# for i in range(1, 101):
#     plik.write(str(i)+"\n")
# plik.close()
# #otwarcie strumienia pliku
# # tryb r - read odczyt
# #tryb w - write zapis
# #tryb - append dopisz
# # w trybie w i a jak wpiszemy nazwę pliku jakiego nie ma to Python go utworzy
# plik = open("dane.txt", "r")
# # odczytywanie pliku 1 sposób
# # print(plik.readline())
# # print(plik.readline())
# # print(plik.readline())
# # print(plik.readline())
#
# # odczytywanie pliku 2 sposób - zwraca liste
# # dane = plik.readlines()
# # print(dane)
# # print(len(dane))
# # for i in dane:
# #     print(i.strip())
#
# #odczytywanie pliku 3 sposób
# for i in plik:
#     print(i.strip())
#
# plik.seek(0)#odczyt pliku od nowa, kursor na początek wraca
# plik.close()
##################################################################
# zapisywanie do pliku
# plik = open("dane.txt", "w")

# dodawanie do pliku 1 sposób write dla pojedynczych danych
# plik.write("2345\n")
# plik.write("artur\n")
# plik.write("malwina\n")

# dodawanie do pliku 2 sposób writelines dla typow sewencyjnych
# lista = ["123\n", "43543\n", "534534\n", "535321\n"]
# plik.writelines(lista)
# plik.close()

# plik = open("dane.txt", "w")
# for i in range(1, 105):
#     plik.write(str(i)+"\n")
# # licznik = 0
# while (True):
#     licznik += 1
#     plik.write(str(licznik) + "\n")
#
#     if licznik == 100:
#         break
###########################################################################
# #dopisywanie do pliku
# plik = open("dane.txt", "a")
#
# plik.write("Robert\n")
# plik.write("art\n")
# plik.write("kil\n")
#
#
# plik.close()


# plik = open("dane.txt", "r")
# wiersz = plik.readline()
# wierszLista = wiersz.split(";")
# print(wierszLista)
# print(f"Imię: {wierszLista[0]} Nazwisko: {wierszLista[1]} Kod: {wierszLista[2].strip()}")
# plik.close()


def dodaj(imie, nazwisko, grupa):
    plik = open("84.txt", "w")
    plik.write(f"{imie};{nazwisko};{grupa}\n")
    plik.close()

def usun():
    plik = open("84.txt", "r")
    daneZPlik = plik.readlines()
    plik.close()
    #szukanie studenta
    znaleziono = False
    for i in daneZPlik:
        lista = i.split(";")
        if lista[1] == nazwisko:
            daneZPlik.remove(i)
            znaleziono = True
            break

    #zapisanie listy do pliku
    if(znaleziono == True):
        plik = open("84.txt", "w")
        plik.writelines(daneZPlik)

        plik.close()
        print("Student został usunięty")
    else:
        print('Nie odnaleziono studenta')

def edytuj():
    plik = open("84.txt", "r")
    daneZPlik = plik.readlines()
    plik.close()
    #szukanie studenta
    znaleziono = False
    for i in daneZPlik:
        lista = i.split(";")
        if lista[1] == nazwisko:

            znaleziono = True
            break
    #zapisanie listy do pliku
    if(znaleziono == True):
        plik = open("84.txt", "w")
        plik.writelines(daneZPlik)

        plik.close()
        print("Student został usunięty")
    else:
        print('Nie odnaleziono studenta')
def pokaz():

    plik = open("84.txt", "r")
    for i in plik:
        lista = i.split(";")
    print(f"Imię: {lista[0]} Nazwisko: {lista[1]} Kod: {lista[2].strip()}")
    plik.close()

while(True):
    menu = input("D-dodaj, P-pokaz, U-usun, K-koniec").upper()

    if(menu == "D"):
        imie = input("Podaj imie studenta: ")
        nazwisko = input("Podaj nazwisko studenta: ")
        grupa = input("Podaj grupę studenta: ")
        dodaj(imie, nazwisko, grupa)

    elif (menu == "P"):
        pokaz(nazwisko)

    elif (menu == "E"):
        nazwisko = input("Podaj nazwisko studenta do edycji: ")
        noweImie = input("Podaj noweImie studenta: ")
        noweNazwisko = input("Podaj noweNazwisko studenta: ")
        edytuj(nazwisko, noweImie, noweNazwisko)


    elif (menu == "U"):
        nazwisko = input("Podaj nazwisko studenta do usuniecia: ")
        if nazwisko ==  nazwisko:
            usun(nazwisko)

    elif (menu == "K"):
        print("koniec")
        break
    else:
        print("Nierozpoznana opcja menu")
