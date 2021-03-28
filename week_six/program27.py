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
print("Vykázané hodiny: \n", reports.groupby("projekt")["hodiny"].sum(), "\n")

# Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.
# Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře,
# tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.
reports_employees = pandas.merge(reports, employees, how="left", on="cislo_zamestnance")
print(reports_employees, "\n")

hours_per_office = reports_employees.groupby(["projekt", "mesto"])["hodiny"].sum()
hours_per_project = reports_employees.groupby(["mesto", "projekt"])["hodiny"].sum()
print("Celkem vykázáno hodin na projektu za kancl: \n", hours_per_office, "\n")
print("Celkem vykázáno hodin na kanclu za projekt: \n", hours_per_project, "\n")
