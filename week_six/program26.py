import requests
import pandas

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv"
p = requests.get(url, allow_redirects=True)
open('zam_praha.csv', 'wb').write(p.content)
prague = pandas.read_csv("zam_praha.csv")

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv"
n = requests.get(url, allow_redirects=True)
open('zam_plzen.csv', 'wb').write(n.content)
pilsen = pandas.read_csv("zam_plzen.csv")

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv"
l = requests.get(url, allow_redirects=True)
open('zam_liberec.csv', 'wb').write(l.content)
liberec = pandas.read_csv("zam_liberec.csv")

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv"
s = requests.get(url, allow_redirects=True)
open('platy_2021_02.csv', 'wb').write(s.content)
salaries = pandas.read_csv("platy_2021_02.csv")

# Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame).
# Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
prague["mesto"] = "Praha"
pilsen["mesto"] = "Plzeň"
liberec["mesto"] = "Liberec"

# Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
employees = pandas.concat([prague, pilsen, liberec], ignore_index=True)

# Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021.
# Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
february_salaries = pandas.merge(employees, salaries, how='outer', on=['cislo_zamestnance'])
print(february_salaries.head())

# Porovnej rozměry tabulek před spojením a po spojení.
# Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
print(salaries.shape)
print(february_salaries.shape)
print(salaries.shape < february_salaries.shape) #True
# rozdíl 13 platů v únorových mzdách znamená, že ve firmě již 13 zamců nepracuje

# Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.
print(february_salaries.groupby("mesto")["plat"].mean())

# BONUS
# Ulož do proměnné počet zaměstnanců, kteří v naší firmě již nepracují.
unemployed = february_salaries[february_salaries["plat"].isnull()]
unemployed_number = unemployed.shape[0]
print(f"Celkem nezaměstnaných v únoru: {unemployed_number}.")


# V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují.
# Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují.
# Tabulku ulož do souboru CSV.
unemployed.to_csv("uz_nepracuji.csv", index=False)
