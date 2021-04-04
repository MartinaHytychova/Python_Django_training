import pandas

temperature = pandas.read_csv("temperature_celsia.csv")
print(temperature.head(), "\n")

# Vyfiltruj si informace o teplotách 13. listopadu 2017.
thirteen = temperature[temperature["Day"] == 13]
print("Teplota 13.11.2017: \n", thirteen, "\n")

# Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
correct_records = thirteen[thirteen["AvgTemperatureCelsia"] != -72.78]
print("Záznamy bez chybných teplot: \n", correct_records, "\n")

# Seřad hodnoty v souboru podle teploty od největší po nejmenší.
sorted_records = correct_records.sort_values("AvgTemperatureCelsia", ascending=False)
print("Seřazené hodnoty od největší po nejmenší: \n", sorted_records, "\n")


# Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou.
print("Prvních pět s nejvyšší teplotou.: \n", sorted_records.head(), "\n")
print("Prvních pět s nejnižší teplotou.: \n", sorted_records.tail(), "\n")
