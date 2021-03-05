class Car:
    def __init__(self, registration_number, brand_type, mileage):
        self.registration_number = registration_number
        self.brand_type = brand_type
        self.mileage = mileage
        self.available = True

    def rent_car(self):
        if self.available:
            self.available = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def get_info(self):
        if self.available:
            return f"Auto značky {self.brand_type}: {self.registration_number}, {self.brand_type} je možné zapůjčit."
        else:
            return "Auto není možné zapůjčit."

peugeot = Car("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Car("1P3 4747", "Škoda Octavia", 41253)

required_car = input("Zadejte požadovanou značku vozu (Peugeot/Škoda): ")

if required_car == "Peugeot":
    print(peugeot.get_info())
    print(peugeot.rent_car())
elif required_car == "Škoda":
    print(skoda.get_info())
    print(skoda.rent_car())
else:
    print(f"Auto značky {required_car} nelze zapůjčit.")

required_car = input("Zadejte požadovanou značku vozu (Peugeot/Škoda): ")
if required_car == "Peugeot":
    print(peugeot.get_info())
    print(peugeot.rent_car())
elif required_car == "Škoda":
    print(skoda.get_info())
    print(skoda.rent_car())
else:
    print(f"Auto značky {required_car} nelze zapůjčit.")
