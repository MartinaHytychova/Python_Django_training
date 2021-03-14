from datetime import datetime

date = input("Vyberte si datum představení a napište zde (např. 1. 8. 2021): ")
converted_date = datetime.strptime(date, "%d. %m. %Y")

number = int(input("Počet vstupenek: "))

first_start = datetime(2021, 7, 1)
first_end = datetime(2021, 8, 10)
second_start = datetime(2021, 8, 11)
second_end = datetime(2021, 8, 31)

if converted_date >= first_start and converted_date <= first_end:
    final_price = 250 * number
    print(f"Máme otevřeno a cena vstupenky činí: {final_price}.")
elif converted_date >= second_start and converted_date <= second_end:
    final_price = 180 * number
    print(f"Máme otevřeno a cena vstupenky činí: {final_price}.")
else:
    print("V této době je letní kino zavřené")
