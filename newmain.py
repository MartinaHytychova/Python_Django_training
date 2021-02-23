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
