import requests
import pandas
import matplotlib.pyplot as plt
from pandas import DataFrame

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv"
s = requests.get(url, allow_redirects=True)
open('twlo.csv', 'wb').write(s.content)
stocks = pandas.read_csv("twlo.csv")

# Výše uvedeným programem načti data o vývoji ceny akcie.
# Vytvoř čárový graf vývoje zavírací ceny akcie (sloupec Close) v čase.

close_price = stocks["Close"]
date = stocks["Date"]

plt.plot(date, close_price)
#plt.show()

# Zkus nyní převést sloupec Date na typ datetime příkazem níže a vytvoř stejný graf jako předtím.
# Porovnej grafy a zjisti, co se změnilo.

date = pandas.to_datetime(date)
plt.plot(date, close_price)
#plt.show()
# na ose x nyní vidíme přehledně datum s rozestupem 2 měsíců

#BONUS
ax = stocks.plot()
ax.set_ylabel("Cena v dolarech")
ax.set_xlabel("Číslo/Index")
ax.set_title("Ceny akcií")
plt.show()


