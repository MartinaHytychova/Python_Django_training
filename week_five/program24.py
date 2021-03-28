import requests
import pandas
import pytemperature

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('temperature.csv', 'wb').write(r.content)

data = pandas.read_csv("temperature.csv")

temp = ['City', 'AvgTemperature']
average = data['AvgTemperature']

# Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.
print(data.head(n=20), "\n")

# Dotaz na měření, která byla provedena v Praze.
# Ve Fahrenheitech, do Celsia bych musela přepočítat skrze rovnici
print(data[data['City'] == 'Prague']['AvgTemperature'], "\n")

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
print(data[average >= 80][temp], "\n")

# Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
print(data[(average >= 60) & (data['Region'] == 'Europe')][temp], "\n")

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
print(data[(average >= 80) | (average <= -20)][temp], "\n")

"""
Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve stupních Celsia. 
Ve svém programu nejprve proveď import modulu pytemperature. 
Nový sloupec pak přidáš do tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek. 
Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. 
Můžeš např. použít funkci f2c z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.
"""
data["AvgTemperatureCelsia"] = pytemperature.f2c(data["AvgTemperature"])

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
print(data[data['AvgTemperatureCelsia'] >= 30][['City', 'AvgTemperatureCelsia']], "\n")

# Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia
# a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
print(data[(data['AvgTemperatureCelsia'] >= 15) & (data['Region'] == 'Europe')]['AvgTemperatureCelsia'], "\n")

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů.
# Jsou některé hodnoty podezřelé?
print(data[(data['AvgTemperatureCelsia'] >= 30) | (data['AvgTemperatureCelsia'] <= -10)], "\n")

"""
V Africe naměřili:
168         Africa  ...          -99.0               -72.78
212          212         Africa  ...          -99.0               -72.78
213          213         Africa  ...          -99.0               -72.78
214          214         Africa  ...          -99.0               -72.78
215          215         Africa  ...          -99.0               -72.78

to je dost podezřelé :D
"""
