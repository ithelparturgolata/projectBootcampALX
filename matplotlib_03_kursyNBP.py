from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Kurs NBP")
root.geometry("700x350")

def wykres():
    liczby = np.random.normal(10000, 200000, 300000)
    plt.hist(liczby, 50)
    plt.show()

button = Button(root, text="Pokaż", command=wykres)
button.pack()
root.mainloop()