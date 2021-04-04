import pandas

staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

staty["population_density"] = staty["population"] / staty["area"]
staty = staty.sort_values(["population_density", "area"], ascending=(False, True))
print(staty.head())