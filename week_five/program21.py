import requests

url = 'https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv'
r = requests.get(url, allow_redirects=True, verify=False)
open('twlo.csv', 'wb').write(r.content)

import pandas
twilio = pandas.read_csv("twlo.csv")

# Zjisti, kolik má soubor řádek a kolik sloupců.
print(twilio.shape)

# Podívej se na 5 řádků s cenami na začátku souboru, využij k tomu funkci iloc i funkci head().
print(twilio.iloc[:5])
print(twilio.head(n=5))

# U akcií nás zajímají především nejnovější ceny. Podívej se na poslední řádek souboru.
print(f"Aktuální cena akcie je: twilio.tail(1).")

# Počet řádků ulož do proměnné pocet_radku jako číslo.
number_rows = len(twilio.index)
print(f"Počet řádků: {number_rows}.")

"""
Načti si tedy první hodnotu zavírací ceny (sloupec Close) v souboru a poslední hodnotu zavírací ceny v souboru. 
Vypočítej, o kolik procent se zvýšila hodnota akcie.
"""

first = twilio.iloc[0, 5:].values[0]
last = twilio.iloc[301, 5:].values[0]
total = 100 * (last - first)
percent = total / first
print(f" Poslední uzavírací cena je oproti první ceně vyšší o {round(percent, 2)} %")

"""
Vyber si sloupec s maximální cenou akcie (sloupec High) za jednotlivé dny pomocí loc nebo iloc jako sérii. 
Na sloupec použij funkci .max(), abys zjistila maximální zaznamenanou cenu akcie za celé období. 
Obdobným způsobem použij funkci .min() na sloupec Low. 
Z těchto hodnot zjistíš maximální rozsah obchodní ceny akcie, což je základ jednoho z akciových ukazatelů (price range).
"""
price = twilio.iloc[0:, 3].values[0:]
maximum = price.max()
minimum = price.min()
print(f" Maximální rozsah cen akcie za období 2020 byl {maximum - minimum} CZK")
