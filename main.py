item = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018}
print(item["title"])
print("Kniha " + item["title"] + " stojí " + str(item["price"])+ ".")
print("Kniha", item["title"], "stojí", item["price"],".")
print(f"Kniha {item['title']} stojí {item['price']}.")

item["weight"] = 1

if "weight" in item:
    print(f"Hmotnost knihy je {item['weight']}.")
else:
    print("Hmotnost nebyla definována.")

sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 5, "Pavča": 3}
print(len(sausages))

# úkol 1
finalMarks = {"Český jazyk": 1, "Matematika": 1, "Dějepis": 1}
print(finalMarks)

# úkol 2
sales = {"Zkus mě chytit": 4165, "Vrah zavolá v deset": 5681, "Zločinný steh": 2565}
sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] = 100
print(sales)

# úkol 3
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

ticket_number = input("Jaké je tvé číslo lístku?")
ticket_number = int(ticket_number)
if ticket_number in tombola:
    print(f"Vyhráváš {tombola[ticket_number]}")
    del tombola[ticket_number]
    print(tombola)
else:
    print("Bohužel, nevyhráváš nic.")

# úkol 4
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
search_key = input("Jak se jmenuješ?")

if search_key in passwords.keys():
    password = input("Heslo:")
    if password in passwords.values():
        print("Vítej")
    else:
        print("Jdi pryč")
else:
    print("Nejsi na seznamu.")
