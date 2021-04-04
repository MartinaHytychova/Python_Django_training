import matplotlib.pyplot as plt
import pandas
import datetime as dt

pocatecni_zustatek = 10_000
pohyby = [746, 52, -749, -63, 71, 958, 157, -1223, -1509, -285, -350, 728, -260, 809, -164, 243, -238, 233, -646, -82, -275, 179, 417, 149, 301, 957, -711, 376, 421, -15, -663]
pohyby[0] += pocatecni_zustatek
datumy = []
for d in range(1, 32):
  novy_datum = dt.date(2019, 3, d)
  datumy.append(novy_datum)
  #datumy = datumy + [novy_datum, ]
print(datumy)

pohyby_na_uctu = pandas.Series(pohyby, index=datumy)
pohyby_na_uctu.cumsum().plot()
#plt.show()

pohyby_na_uctu.plot(kind='bar', color='yellow', grid=True)
# plt.show()

fig = pohyby_na_uctu.cumsum().plot(grid=True, legend=True)
fig.set_ylabel('Zůstatek v korunách')
fig.set_xlabel('Datum')
plt.ylim(-2000, 2000)
plt.show()
