import pandas
import matplotlib.pyplot as plt

temperature = pandas.read_csv("temperature_celsia.csv")

# Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.

helsinki = temperature[temperature['City'] == 'Helsinki']
miami_beach = temperature[temperature['City'] == 'Miami Beach']
tokyo = temperature[temperature['City'] == 'Tokyo']

temperature_new = pandas.concat([helsinki, miami_beach, tokyo], ignore_index=True)
temperature_new.to_csv("teploty_nove.csv", index="City")

# Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.

data = helsinki['AvgTemperatureCelsia'].to_frame(name='Helsinki')
data.reset_index(drop=True, inplace=True)

miami_beach = miami_beach['AvgTemperatureCelsia']
miami_beach.reset_index(drop=True, inplace=True)
data['Miami Beach'] = miami_beach

tokyo = tokyo['AvgTemperatureCelsia']
tokyo.reset_index(drop=True, inplace=True)
data['Tokyo'] = tokyo

print(data)

data.plot(kind='box', whis=[0, 100])
plt.show()

