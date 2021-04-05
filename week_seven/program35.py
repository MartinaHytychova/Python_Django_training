import pandas
import matplotlib.pyplot as plt

temperature = pandas.read_csv("temperature_celsia.csv")
print(temperature.head(), "\n")

# Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
celsia = ['Region', 'City', 'AvgTemperatureCelsia']
helsinki = temperature[(temperature['City'] == 'Helsinki')][celsia]
miami_beach = temperature[(temperature['City'] == 'Miami Beach')][celsia]
tokyo = temperature[(temperature['City'] == 'Tokyo')][celsia]

temperature_new = pandas.concat([helsinki, miami_beach, tokyo], ignore_index=True)
temperature_new.to_csv("teploty_nove.csv", index="City")
print(temperature_new)

# Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.

data = temperature_new['AvgTemperatureCelsia'].to_frame(name='Helsinki')
data['Miami Beach'] = temperature_new['AvgTemperatureCelsia']
data['Tokyo'] = temperature_new['AvgTemperatureCelsia']
data.plot(kind='box', whis=[0, 100])
plt.show()
