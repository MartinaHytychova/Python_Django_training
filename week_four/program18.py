from datetime import datetime


class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Person(Contact):
    def __init__(self, name, email, date):
        super(Person, self).__init__(name, email)
        self.date = date
        self.note = ""

    def save_note(self, text_note):
        current_date = datetime.now()
        meeting_date = datetime.strptime(self.date, "%d. %m. %Y")
        if meeting_date >= current_date:
            self.note = text_note
            return f"Zápis z pohovoru uchazeče {self.name} se úspěšně uložil."
        else:
            return f"Pohovor s uchazečem {self.name} bude probíhat dne {self.date}."


jan = Person("Jan Novotný", "jan.nov@gmail.com", "10. 11. 2021")
pavel = Person("Pavel Novotný", "pav.nov@gmail.com", "10. 11. 2020")
print(jan.save_note("Ukázal velice vydařený projekt z VŠ."))
print(pavel.save_note("Měl 5 minut  zpoždění, zadané úkoly vypracoval ku spokojenosti managera."))
