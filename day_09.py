haslo = input("Podaj haslo") #samolot
odganiete = set()

while(True):

    koniec = True
    for i in haslo:
        if(i in odganiete):
            print(i, end=" ")
        else:
            print("*", end=" ")
            koniec = False

    print("\n")

    if (koniec == True):
        print("Dzieki za gre !")
        break

    literka = input("Podaj dowolna literke")
    odganiete.add(literka)
