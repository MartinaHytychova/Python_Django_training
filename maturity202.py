import requests
import pandas

url = "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv"
r = requests.get(url, allow_redirects=True)
open('jmena.csv', 'wb').write(r.content)

url = "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv"
r = requests.get(url, allow_redirects=True)
open('u203.csv', 'wb').write(r.content)

url = "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv"
r = requests.get(url, allow_redirects=True)
open('u202.csv', 'wb').write(r.content)

url = "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv"
r = requests.get(url, allow_redirects=True)
open('u302.csv', 'wb').write(r.content)

url = "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv"
r = requests.get(url, allow_redirects=True)
open('studenti.csv', 'wb').write(r.content)

url = "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv"
r = requests.get(url, allow_redirects=True)
open('predsedajici.csv','wb').write(r.content)

u202 = pandas.read_csv('u202.csv').dropna()
u203 = pandas.read_csv('u203.csv').dropna()
u302 = pandas.read_csv('u302.csv').dropna()
studenti = pandas.read_csv('studenti.csv')
print(studenti.head())

u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"

print(u202.reset_index)

maturita = pandas.concat([u202, u203, u302], ignore_index=True)
studenti = pandas.read_csv('studenti.csv')
maturita_se_jmeny = pandas.merge(maturita, studenti, how="left")
preds = pandas.read_csv('predsedajici.csv')
preds["den"] = preds["den"].str.strip()
maturita_se_jmeny_a_predsedy = pandas.merge(maturita_se_jmeny, preds, on=["den"])
maturita_se_jmeny_a_predsedy = maturita_se_jmeny_a_predsedy.rename(columns={"jmeno_x": "jmeno", "jmeno_y": "jmeno_predsedy"})

print(maturita_se_jmeny_a_predsedy.sort_values(by=["datum", "cisloStudenta"]))
print(pandas.to_datetime(maturita_se_jmeny_a_predsedy["datum"], format="%d.%m.%Y"))