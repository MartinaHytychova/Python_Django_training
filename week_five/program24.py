import requests
import pandas
#import pytemperature

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('temperature.csv', 'wb').write(r.content)

data = pandas.read_csv("temperature.csv")

temp = ['City', 'AvgTemperature']

# Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.
print(data.head(n=20))

# Dotaz na měření, která byla provedena v Praze.
# Ve Fahrenheitech, do Celsia bych musela přepočítat skrze rovnici
print(data[data['City'] == 'Prague']['AvgTemperature'])

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
print(data[data['AvgTemperature'] >= 80][temp])

# Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).


# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.

