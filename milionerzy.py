#gra Milionerzy ver 1.0
import random
import sys
imieGracz1 = input("Podaj imię Zawodnika nr 1: ")
imieGracz2 = input("Podaj imię Zawodnika nr 2: ")
imieGracz3 = input("Podaj imię Zawodnika nr 3: ")
imieGracz4 = input("Podaj imię Zawodnika nr 4: ")
imieGracz5 = input("Podaj imię Zawodnika nr 5: ")
imieGracz6 = input("Podaj imię Zawodnika nr 6: ")
imieGracz7 = input("Podaj imię Zawodnika nr 7: ")
imieGracz8 = input("Podaj imię Zawodnika nr 8: ")
listaGracze = []
listaGracze.append(imieGracz1)
listaGracze.append(imieGracz2)
listaGracze.append(imieGracz3)
listaGracze.append(imieGracz4)
listaGracze.append(imieGracz5)
listaGracze.append(imieGracz6)
listaGracze.append(imieGracz7)
listaGracze.append(imieGracz8)
print("\nGracze biorący udział w teleturnieju to: ", listaGracze)
gracz = random.choice(listaGracze)
print("\nOsoba wylosowana do udziału w turnieju głównym: ", gracz)
wygrane = ["0 zł", "500 zł", "1.000 zł", "2.000 zł", "5.000 zł", "10.000 zł", "20.000 zł", "40.000 zł", "75.000 zł", "125.000 zł", "250.000 zł", "500.000 zł", "1.000 000"]
pytanie1 = {1: "Gniezno", 2: "Lublin", 3: "Warszawa", 4: "Kraków"}
pytanie2 = {1: "Paul", 2: "Steve", 3: "James", 4: "John"}
pytanie3 = {1: "z Mordoru",  2: "z Oz",  3: "z Rivii", 4: "z Cimmerii"}
pytanie4 = {1: "Na djembe", 2: "Na kornecie", 3: "Na akordeonie", 4: "Na ksylofonie"}
pytanie5 = {1: "W Szwajcarii", 2: "Anhelli", 3: "Godzina myśli", 4: "Arab"}
pytanie6 = {1: "spać", 2: "pracować", 3: "śpiewać", 4: "podróżować"}
pytanie7 = {1: "Kanadyjczycy", 2: "Szwedzi", 3: "Rosjanie", 4: "Chińczycy"}
pytanie8 = {1: "obręcz z dętką", 2: "dętkę z piastą", 3: 'piastę z obręczą', 4: "obręcz z widelcem"}
pytanie9 = {1: "Simba", 2: "Tołstoj", 3: "Trocki", 4: "Mufasa"}
pytanie10 = {1: "Z wiśni", 2: "Z jabłka", 3: "Z gruszki", 4: "Z Moreli"}
pytanie11 = {1: "Moje Bermudy Stal Gorzów", 2: "Betard Sparta Wrocław", 4: "Fogo Unia Leszno"}
pytanie12 = {1: "tlenek cynku", 2: "szkielet ryb karpiowatych", 3: "łupki bitumiczne", 4: "tran"}

charPytanie1 = int(input(f"\nPierwsza stolica Polski to: {pytanie1} " ))
if charPytanie1 == 1 in pytanie1:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[1])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[0])
    sys.exit()

charPytanie2 = int(input(f"\nJak miał na imię slynny brytyjski muzyk Lennon: {pytanie2} " ))
if charPytanie2 == 4 in pytanie2:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[2])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[0])
    sys.exit()

charPytanie3 = int(input(f"\nSkąd pochodzi Conan Barbarzyńca: {pytanie3} " ))
if charPytanie3 == 4 in pytanie3:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[3])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[2])
    sys.exit()

charPytanie4 = int(input(f"\nZ gry na jakim instrumencie słynie Czesław Mozil: {pytanie4} " ))
if charPytanie4 == 3 in pytanie4:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[4])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[2])
    sys.exit()

charPytanie5 = int(input(f"\nKtóry utwór Juliusza Słowackiego napisany jest prozą: {pytanie5} " ))
if charPytanie5 == 2 in pytanie5:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[5])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[2])
    sys.exit()

charPytanie6 = int(input(f"\nNa akord można: {pytanie6} " ))
if charPytanie6 == 2 in pytanie6:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[6])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[2])
    sys.exit()

charPytanie7 = int(input(f"\nKto na igrzyskach olimpijskich w Pjongczangu nie mógł startować pod flagą własnego kraju: {pytanie7} " ))
if charPytanie7 == 3 in pytanie7:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[7])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[2])
    sys.exit()

charPytanie8 = int(input(f"\nCo łączy rowerowa szprycha: {pytanie8} " ))
if charPytanie8 == 3 in pytanie8:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[8])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[7])
    sys.exit()

charPytanie9 = int(input(f"\nLew zabity przez Ramona Mercadera to: {pytanie9} " ))
if charPytanie9 == 2 in pytanie9:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[9])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[7])
    sys.exit()

charPytanie10 = int(input(f"\nLikier maraskino produkuje się z maraski, czyli odmiany: {pytanie10} " ))
if charPytanie10 == 1 in pytanie10:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[10])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[7])
    sys.exit()

charPytanie11 = int(input(f"\nDrużynowym Mistrzem Polski na żużlu w 2020 jest: {pytanie11} " ))
if charPytanie11 == 4 in pytanie11:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[11])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[7])
    sys.exit()

charPytanie12 = int(input(f"\nCo jest głównym składnikiem maści ichtiolowej: {pytanie12} " ))
if charPytanie12 == 3 in pytanie12:
    print(f"Brawo prawidłowa odpowiedź." + " " + "Gramy dalej. " + str(gracz) + " " + "wygrywasz:" + " " + wygrane[12])
else:
    print("Niestety błędna odpowiedź. Zakończył Pan grę wygrywając", wygrane[7])
    sys.exit()