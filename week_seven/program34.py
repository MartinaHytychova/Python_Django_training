import requests
import pandas
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv"
s = requests.get(url, allow_redirects=True)
open('velikonoce.csv', 'wb').write(s.content)
easter_data = pandas.read_csv("velikonoce.csv")

# Vytvoř sloupcový graf, který data přehledně zobrazí.
# Na ose x budou vidět jednotlivá data ("datumy") a výška sloupce označí,
# kolikrát na daný den připadly Velikonoce.

date = easter_data['Datum']
count = easter_data['Počet']

plt.plot(date, count)
ax = easter_data.plot()
ax.set_ylabel("Kolikrát Velikonoc")
ax.set_xlabel("Datum")
ax.set_title("Velikonoce")
plt.show()

# BONUS

# Vytvoř si datový soubor sama.
# Můžeš k tomu využít modul dateutil, který při instalaci najdeš pod jménem python-dateutil.
# Následně si zkopíruj kód níže a doplň na místo komentářů příkazy, které prováději požadovanou činnost.

from dateutil import easter

data = []
for rok in # sem doplň funkci range
  datum = easter.easter(rok)
  # Naformátuj datum jako řetězec tak, aby obsahovalo jen měsíc a den. Měsíc dej na začátek a za něj den - použij funkci strftime, kterou jsme spolu probírali
  # Naformátovaný datum ulož do seznamu data

data = pandas.DataFrame(data, columns=["Datum"])
data = data.groupby("Datum").size()