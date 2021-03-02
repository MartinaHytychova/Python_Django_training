results = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

"""

"Prospěl s vyznamenáním", pokud je průměr jeho známek maximálně 1.5 a nemá žádnou trojku.
"Neprospěl", pokud má alespoň jednu pětku.
"Prospěl", pokud nemá vyznamenání a současně nedostal žádnou pětku.

Přidej funkci ohodnot_studenta(), která bude mít jeden parametr, kterým je slovník se známkami studenta. 
Funkce rozhodne, zda student prospěl, prospěl s vyznamenáním nebo neprospěl podle výše popsaných kritérií.

Dále napiš cyklus, který projde seznam vysledky a pomocí funkce ohodnot_studenta() zjistí prospěch studenta. 
Následně pro každého studenta vypíše jeho jméno a informaci o tom, zda prospěl, neprospěl či prospěl s vyznamenáním.

"""
exists = False
marks = {}

for result in results:
  count = 0
  marks = result
  name = result["Jméno"]
  result.pop("Jméno")
  exists = True
  for k, v in marks.items():
    count += v
  final_mark = count / 5
  print(name, final_mark)