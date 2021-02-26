sales2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}

book = input("Zadejte název knihy:")

if book in sales2019 and book in sales2020:
    print(f"Tato kniha se v roce 2019 a 2020 prodala v počtu: {sales2019[book] + sales2020[book]}")
elif book in sales2020:
    print(f"Tato kniha se v roce 2020 prodala v počtu: {sales2020[book]}")
else:
    print("Taková kniha není v záznamech")
