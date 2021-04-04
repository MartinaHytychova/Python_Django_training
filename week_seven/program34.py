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

