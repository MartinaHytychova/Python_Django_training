class Employee:
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}. " \
               f"Hrubá mzda činí {self.wage}, " \
               f"při počtu dětí {self.children} je čistá mzda celkem: {self.get_net_salary()} Kč."

    def __init__(self, name, position, wage, children):
        self.name = name
        self.position = position
        self.wage = wage
        self.children = children

    def get_tax(self):
        tax = self.wage * 0.15 - self.children * 1500
        if tax < 0:
            return 0
        return tax

    def get_net_salary(self):
        return self.wage - self.get_tax()

petr = Employee("Petr Pavel", "Pope", 40000, 0)
karel = Employee("Karel Gott", "Singer", 100000, 3)

print(petr.get_info())
print(karel.get_info())
