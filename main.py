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

sales = {
    "Zkus mě chytit": 254,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
total = 0
for key, value in sales.items():
    print(f"Knihy {key} se prodalo {value} kusů.")
total += value
# total = total + value
print(f"Celkem bylo prodáno {total} knih.")
print("Celkem bylo prodáno " + str(total) + " knih.")


books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
total = 0
for item in books:
    total += item["sold"] * item["price"]
print(f"Celkové tržby jsou {total}.")

sum_marks = 0
subjects = []
for subject, mark in schoolReport.items():
    sum_marks += mark

    if mark == 1:
        subjects.append(subject)

print(', '.join(subjects))
print(sum_marks / len(schoolReport))
print(sum(schoolReport.values()) / len(schoolReport))

def getMark(points):
  if points <= 60:
    mark = 5
  elif points <= 70:
    mark = 4
  elif points <= 80:
    mark = 3
  elif points <= 90:
    mark = 2
  else:
    mark = 1
  return mark

points = input("Zadej počet bodů: ")
points = int(points)
mark = getMark(points)

if mark == 5:
  points = input("Počet bodů z opravného testu: ")
  points = int(points)
  mark = getMark(points)
print(f"Výsledná známka je {mark}.")

def getMark(points, bonus=0):
  if points + bonus <= 60:
    mark = 5
  elif points + bonus <= 70:
    mark = 4
  elif points + bonus <= 80:
    mark = 3
  elif points + bonus <= 90:
    mark = 2
  else:
    mark = 1
  return mark

points = input("Zadej počet bodů: ")
points = int(points)
bonus = input("Zadej počet bonusových bodů: ")
bonus = int(bonus)
mark = getMark(points, bonus)

if mark == 5:
  points = input("Počet bodů z opravného testu: ")
  points = int(points)
  mark = getMark(points)
print(f"Výsledná známka je {mark}.")

from datetime import datetime,timedelta
datetime.now()
datetime.datetime(2021, 3, 2, 20, 7, 19, 770468)
apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start)
1969-07-16 14:32:00
apollo_start.weekday()
2
apollo_start.isoweekday()
3
apollo_start.isoformat()
'1969-07-16T14:32:00'
apollo_start.strftime("%d, %m, %Y, %H, %M")
'16, 07, 1969, 14, 32'
apollo_start.strftime("%d. %m. %Y, %H:%M")
'16. 07. 1969, 14:32'
apollo_start.strftime("%d. %m. %Y, %H:%M hod")
'16. 07. 1969, 14:32 hod'
apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M hod")
apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
delka_mise = apollo_pristani - apollo_start
print(delka_mise)
5 days, 4:22:00


"""

 Převod času
V proměnné apolloStart máme uložený datum a čas startu Apolla 11. 
Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané, 
tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka. 
Čas vypisovat nemusíš.

apollo_start.strftime("%m/%d/%Y, %I:M% %p")


¶ Čas od startu
Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03. 
Ulož si hodnotu startu do proměnné.

Který den v týdnu Solar Orbiter odstartoval?
Spočítej, kolik času od jeho startu uplynulo.


¶ Doprava večeře
Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47. 
Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund, 
příprava jídla trvá 30 minut a doprava jídla k zákazníkovi 25 minut a 30 sekund. 
Kdy očekáváme, že jídlo dorazí zákazníkovi?

"""

class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25


class PartTimeEmployee(Employee):
  def getInfo(self):
    return "Je to brigádník."
  def __init__(self, name, position, workload):
    super().__init__(name, position)
    self.workload = workload

    brigadnik = PartTimeEmployee("Jirka Pesik", "brigadnik ve skladu", 0.5)
    print(brigadnik.getInfo())

    class Package:
        def __init__(self, address, weight):
            self.address = address
            self.weight = weight
            self.delivered = False

        def deliver(self):
            self.delivered = True

        def get_info(self):
            return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}'
