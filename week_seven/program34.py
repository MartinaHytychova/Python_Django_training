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
ax = easter_data.plot(x='Datum', kind='bar')
ax.set_ylabel("Počet Velikonoc")
ax.set_xlabel("Dny")
ax.set_title("Velikonoce mezi lety 1600 - 2100")
# plt.show()

# BONUS

# Vytvoř si datový soubor sama.
# Můžeš k tomu využít modul dateutil, který při instalaci najdeš pod jménem python-dateutil.
# Následně si zkopíruj kód níže a doplň na místo komentářů příkazy, které prováději požadovanou činnost.

from dateutil import easter

data = []
for rok in range(1600, 2100):
    datum = easter.easter(rok)
    # Naformátuj datum jako řetězec tak, aby obsahovalo jen měsíc a den.
    # Měsíc dej na začátek a za něj den - použij funkci strftime, kterou jsme spolu probírali
    datum = datum.strftime("%m-%d")
    data += [datum]

data = pandas.DataFrame(data, columns=["Datum"])
data = data.groupby("Datum").size()
print(data)
