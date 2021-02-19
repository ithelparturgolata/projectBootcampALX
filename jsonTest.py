from tkinter import *
import requests
from tkinter import messagebox
import tkinter as tk
import json

class Sample():

    def getData(self):

        self.res = requests.get(f"https://api.chucknorris.io/jokes/random")
        self.data = self.res.json()
        self.result["text"] = self.data['value']

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1900x200")
        self.root.title("Chuck Norris jokes")
        #self.root.resizable(0,0)
        self.font = ("Verdana", 10, "bold")

        self.header = Label(self.root, width = 1000, height = 2, bg = "#666699", font = self.font)
        self.header.place(x = 0, y = 0)

        self.heading = Label(self.root, text = " Chuck Norris jokes",  font = self.font)
        self.heading.place(x = 120, y = 5)

        self.button = Button(self.root, text="Losuj", font= self.font, command=self.getData, bg="#666699", fg="white")
        self.button.place(x=10, y=80)

        self.display = Label(self.root, text="Wynik:" , bg="#669999", font = self.font)
        self.display.place(x=10, y=160)

        self.result = Label(self.root, text="???",  font=self.font)
        self.result.place(x=90, y=160)

        self.root.mainloop()

if __name__ == '__main__':
    Sample()


# import requests
# category = input("Podaj kategorię: ")
# res = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
# dane2 = res.json()
# print(dane2['value'])
