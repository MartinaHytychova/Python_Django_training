import requests
import pandas
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv"
s = requests.get(url, allow_redirects=True)
open('platy.csv', 'wb').write(s.content)
salaries = pandas.read_csv("platy.csv")

salaries.hist(bins=[
  150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210
])
plt.show()