#graficzna analiza połączeń SM Budowlani
import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25
plt.figure(figsize=(16,8))

bars1 = [2792, 2935, 3203, 2928, 3661]
bars2 = [1616, 1726, 1769, 1905, 2095]
bars3 = [1176, 1209, 1434, 1023, 1566]


r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]


plt.bar(r1, bars1, color='grey', width=barWidth, edgecolor='white', label='Wszystkie')
plt.bar(r2, bars2, color='blue', width=barWidth, edgecolor='white', label='Odebrane')
plt.bar(r3, bars3, color='lightgreen', width=barWidth, edgecolor='white', label='Nieodebrane')


plt.title("Wykaz połączeń: Administracja Ogólna")
plt.xlabel("Miesiąc", fontweight='bold')
plt.ylabel("Ilość połączeń", fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik'])


plt.legend()
plt.show()