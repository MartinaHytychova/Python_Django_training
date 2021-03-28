import pandas

temperature = pandas.read_csv("temperature_celsia.csv")
print(temperature.head(), "\n")

# Vyfiltruj si informace o teplotách 13. listopadu 2017.
thirteen = temperature[temperature["Day"] == 13]
print("Teplota 13.11.2017: \n", thirteen, "\n")

# Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
correct_records = thirteen[thirteen["AvgTemperatureCelsia"] != -72.78]
print("Záznamy bez chybných teplot: \n", correct_records, "\n")

# Vypočti počet dat, které máš daný den za jednotlivé regiony.
print("Počet dat za reg.: \n", correct_records.groupby(["Region"])["AvgTemperatureCelsia"].count(), "\n")

# Vypočti průměrnou teplotu za jednotlivé regiony.
print("Průměrná teplota za reg.: \n", round(correct_records.groupby(["Region"])["AvgTemperatureCelsia"].mean(), 2), "\n")

# Vypočti maximální a minimální teplotu v každém regionu.
print("Minimální teplota za reg.: \n", round(correct_records.groupby(["Region"])["AvgTemperatureCelsia"].min(), 2), "\n")
print("Maximální teplota za reg.: \n", round(correct_records.groupby(["Region"])["AvgTemperatureCelsia"].max(), 2), "\n")
