#import wget
#wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")

import pan
nakupy = pan.read_csv("nakupy.csv")
"""
print(nakupy.info())
print(nakupy.shape[0])
print(nakupy.columns)
print(nakupy.iloc[3])
pozdrav = " Ahoj  Andreo  "
print(pozdrav.strip().replace("  ", " "))
"""

print(nakupy.head(n=3))
print(nakupy.tail(n=2))

print(nakupy.iloc[:5, 0])


wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")
import pan
import wget

wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")
staty = pan.read_json("staty.json")
staty = staty.set_index("name")

pidistaty = staty[staty["population"] < 1000]
print(pidistaty[["area", "population"]])

lidnate_evropske_staty = staty[(staty["population"] > 20_000_000) & (staty["region"] == "Europe")]
print(lidnate_evropske_staty["population"])