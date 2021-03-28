import requests
import pandas
import pytemperature

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('temperature.csv', 'wb').write(r.content)

data = pandas.read_csv("temperature.csv")
data["AvgTemperatureCelsia"] = pytemperature.f2c(data["AvgTemperature"])

# Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky. Dále napiš následující dotazy:
print(data.head(n=20), "\n")
celsia = ['Region', 'City', 'AvgTemperatureCelsia']

# Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
print(data[data['Day'] == 13][celsia], "\n")

# Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US).
# Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
usa = data[(data['Day'] == 13) & (data['Country'] == 'US')][celsia]

# Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.
print(usa[(usa['City'] == 'Washington') | (usa['City'] == 'Philadelphia')][celsia], "\n")

# Vrať se k pomocné tabulce, kterou jsi vytvořila v bodu 2.
# Vypiš průměrnou hodnotu ze všech měření, která byla provedena 13. listopadu 2017 na území Spojených států amerických.
# K tomu využij funkci .mean(), která funguje stejně jako funkce .sum(), kterou jsme si ukazovali na lekci.
avg = usa.mean()
print(f"Průměr teplot ze 13. listopadu 2017 na území Spojených států amerických činí {round(avg.values[0], 2)} Celsia.\n")

# Pokud znáš základy statistiky, zkus funkci pro medián .median() a rozptyl .var().
median = usa.median()
print(f"Medián teplot ze 13. listopadu 2017 na území Spojených států amerických činí {round(median.values[0], 2)} Celsia.\n")

range = usa.var()
print(f"Rozptyl teplot ze 13. listopadu 2017 na území Spojených států amerických činí {round(range.values[0], 2)} Celsia.\n")
