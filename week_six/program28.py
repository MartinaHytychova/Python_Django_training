import requests
import pandas

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json"
s = requests.get(url, allow_redirects=True)
open('staty.json', 'wb').write(s.content)
states = pandas.read_json("staty.json")

url = "https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv"
h = requests.get(url, allow_redirects=True)
open('hdp.csv', 'wb').write(h.content)

# Načti data ze souboru do tabulky.
states = pandas.read_json("staty.json").dropna()
gdp = pandas.read_csv("hdp.csv").dropna()
print("Státy: \n", states.head(), "\n")

# Vyfiltruj státy, které leží v Evropě.
print("Státy v Evropě: \n", states[states["region"] == "Europe"], "\n")

# Zjisti počet států v jednotlivých subregionech Evropy.
print("Počet ev. států v subreg.: \n", states[states["region"] == "Europe"].groupby(["region", "subregion"])["subregion"].count(), "\n")

# Zjisti celkový počet obyvatel v jednotlivých subregionech Evropy.
print("Celk. počet obyv. ev. států v subreg.: \n", states[states["region"] == "Europe"].groupby(["region", "subregion"])["population"].sum(), "\n")

# BONUS
# Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy,
# které nemají kompletní informace GDP (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).
print("HDP: \n", gdp.head(), "\n")

# Propoj obě tabulky podle třípísmenného kódu států.
states_key = states.rename(columns={"alpha3Code": "Country Code"})
complete_table = pandas.merge(gdp, states_key, on="Country Code", how="left")

# Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.
sub = complete_table.groupby(["subregion"])[["2019", "population"]].sum()
print("Celkové HDP za 2019: \n", sub, "\n")

# Projdi si subkapitolu o počítaných sloupcích (část o podmínených sloupcích není nutné číst).
# K tabulce, kterou jsi vytvořila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele,
# tj. přidej sloupec s velikostí GDP v roce 2019 vydělenou počtem obyvatel daného subregionu.
sub["hdp_2019"] = sub["2019"] / sub["population"]
print("Výše HDP na obyvatele v roce 2019: \n", sub)
