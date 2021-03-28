import requests
import pandas

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('character_deaths.csv', 'wb').write(r.content)

data = pandas.read_csv("character_deaths.csv")

# Načti soubor do tabulky (DataFrame) a nastav sloupec Name jako index
death_char = data.set_index('Name')
print(death_char, "\n")

# Zobraz si sloupce, které tabulka má.
# Posledních pět sloupců tvoří zkratky názvů knih a informace o tom, jestli se v knize postava vyskytuje.
for col in death_char.columns:
    print(col, "\n")

# Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".
print(death_char.loc['Hali'], "\n")

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
print(death_char.loc['Gevin Harlaw':'Gillam'], "\n")

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.
print(death_char.loc['Gevin Harlaw':'Gillam', 'Death Year'], "\n")

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v jakých knihách se postava vyskytuje,
# tj. vypiš všechny sloupce mezi GoT a DwD.
print(death_char.loc['Gevin Harlaw':'Gillam', 'GoT':], "\n")
