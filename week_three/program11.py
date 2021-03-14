class Car:
    def __init__(self, registration_number, brand_type, mileage):
        self.registration_number = registration_number
        self.brand_type = brand_type
        self.mileage = mileage
        self.available = True

peugeot = Car("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Car("1P3 4747", "Škoda Octavia", 41253)
citroen = Car("2S3 2335", "Citroen Xsara", 3452)
