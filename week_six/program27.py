import requests
import pandas

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv"
r = requests.get(url, allow_redirects=True)
open('vykazy.csv', 'wb').write(r.content)
reports = pandas.read_csv("vykazy.csv")

# Načti data ze souboru a ulož je do tabulky.
# Načtení tabulky z minulého souboru a dat z nové tabulky vykazy
employees = pandas.read_csv("vsichni_zamci.csv")
reports = reports.rename(columns={"date": "datum", "hours": "hodiny", "project": "projekt", "emloyee_id": "cislo_zamestnance"})
reports = reports.set_index("cislo_zamestnance")
print(reports.head(), "\n")

# Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
print("Vykázané hodiny: ", reports.groupby("projekt")["hodiny"].sum(), "\n")

# Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.
# Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře,
# tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.

