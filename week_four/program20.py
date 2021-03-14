from faker import Faker
fake_data = Faker(['cs_CZ', 'sk_SK'])


class Package:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu: {self.address}")

  def __init__(self, name, address):
    self.name = name
    self.address = address

for _ in range(2):
    potraviny = Package(fake_data.name(), fake_data.address())
    print(potraviny.get_info())
