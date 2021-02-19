class Koszyk:

    def __init__(self):
        self.zakupy = {}

    def dodajProdukt(self, produkt, ilosc):
        koszyk = Koszyk(produkt, ilosc)


    def usunProdukt(self, produkt, ilosc):
        pass


magazyn = {"chleb": 20, "woda": 1.20, "jogurt": 3.45}
koszyk = Koszyk()

while (True):

    menu = input("D-dodaj, U-usun, P-podglad, K-kasa")
    if (menu == "D"):
        produkt = input("Podaj nazwę produktu")
        ilosc = input("Podaj ilość")

    elif (menu == "U"):
        pass
    elif (menu == "P"):
        pass
    elif (menu == "K"):
        pass
    else:
        print("Nierozpoznana opcja menu.")

