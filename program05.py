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

# Vraťme se k software pro našeho nakladatele.
# Nakladatel má nyní v software dva slovníky,
# které obsahují informace o prodejích knih v letech 2019 a 2020.
#
# Uvažuj, že uživatel se zajímá o prodeje konkrétní knihy.
# Zeptej se uživatele na název knihy a poté vypiš informaci o tom,
# kolik se této knihy celkem prodalo.
# Nezapomeň na to, že některé knihy byly prodávány pouze v jednom roce.

book = input("Zadejte název knihy:")

for key, value in list(sales2020.items()):
    if book in sales2019.keys() and sales2020.keys():
        print(sales2019[book] + sales2020[book])
        break
    elif book in sales2019.keys() or sales2020.keys():
        print(sales2020[book] or sales2019[book])
        break


