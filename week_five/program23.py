import requests
import pandas

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('country_vaccinations.csv', 'wb').write(r.content)

data = pandas.read_csv("country_vaccinations.csv")

col = ['country', 'total_vaccinations']

# Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10
print(data[(data['date'] == '2021-03-10')][col])

# Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel.
print(data[(data['date'] == '2021-03-10') & (data['total_vaccinations'] > 1000000)][col])

# Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí nebo naopak méně než 100 lidí.
in_range = (data['date'] == '2021-03-10') & ((data['total_vaccinations'] > 100000) | (data['total_vaccinations'] < 100))
print(data[in_range][col])

# Vypiš informace o očkování za dny 2021-03-10 a 2021-03-11 pro státy United Kingdom, Finland a Italy. Použij např. funkci isin().
countries = data['country'].isin(['Italy', 'Finland', 'United Kingdom'])
dates = (data['date'] == '2021-03-10') | (data['date'] == '2021-03-11')
print(data[countries & dates][col])

# Vypiš informace o očkování pro Japan mezi daty 2021-03-03 a 2021-03-09.
# Data v tomto formátu můžeš porovnávat pomocí operátorů >= a <= jako řetězce
japan_dates = (data['date'] >= '2021-03-03') & (data['date'] <= '2021-03-09') & (data['country'] == 'Japan')
print(data[japan_dates][['date', 'total_vaccinations']])
