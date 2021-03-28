import requests
import pandas

url = "https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti1.csv"
r = requests.get(url, allow_redirects=True)
open('studenti1.csv', 'wb').write(r.content)

url = "https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti2.csv"
r = requests.get(url, allow_redirects=True)
open('studenti2.csv', 'wb').write(r.content)
url = "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv"
r = requests.get(url, allow_redirects=True)
open('jmena.csv', 'wb').write(r.content)

studenti1 = pandas.read_csv("studenti1.csv")
studenti2 = pandas.read_csv("studenti2.csv")
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
# print(studenti)
# print(studenti.shape)
nestuduje = studenti[studenti["ročník"].isnull()].shape[0]
dalkovy = studenti[studenti["kruh"].isnull()].shape[0]
# print(f"Ze seznamu studentu jiz {nestuduje} studentu nestuduje a {dalkovy} studentu studuje dalkove.")
studenti = studenti.dropna(subset=["ročník","kruh"])
# print(studenti.shape)
# print(studenti.groupby("obor").count())
# print(studenti.groupby("obor")["prospěch"].mean())
jmena = pandas.read_csv("jmena.csv")
studenti_jmena = pandas.merge(studenti,jmena)
# print(studenti_jmena)
# print(studenti_jmena.groupby("pohlaví").count())