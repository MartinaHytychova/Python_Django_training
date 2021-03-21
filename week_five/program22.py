import requests

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('character_deaths.csv', 'wb').write(r.content)

import pandas
data = pandas.read_csv("character_deaths.csv")

# Načti soubor do tabulky (DataFrame) a nastav sloupec Name jako index
death_char = pandas.DataFrame(data=data).set_index('Name')
print(death_char)

# Zobraz si sloupce, které tabulka má.
# Posledních pět sloupců tvoří zkratky názvů knih a informace o tom, jestli se v knize postava vyskytuje.
for col in death_char.columns:
    print(col)

# Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".
hali = death_char.loc['Hali']
print(hali)

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
range = death_char.loc['Gevin Harlaw':'Gillam']
print(range)

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.
death_range = death_char.loc['Gevin Harlaw':'Gillam', 'Death Year']
print(death_range)

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v jakých knihách se postava vyskytuje,
# tj. vypiš všechny sloupce mezi GoT a DwD.
book_range = death_char.loc['Gevin Harlaw':'Gillam', 'GoT':]
print(book_range)
