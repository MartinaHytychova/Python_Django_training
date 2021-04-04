import requests
import pandas
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv"
s = requests.get(url, allow_redirects=True)
open('platy.csv', 'wb').write(s.content)
salaries = pandas.read_csv("platy.csv")

salaries = salaries["plat"]
salaries.hist(bins=[
  30000, 32500, 35000, 37500, 40000, 42500, 45000, 47500, 50000, 52500, 55000, 57500, 60000
])
plt.show()
