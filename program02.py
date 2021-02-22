warehouse = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

code = input("Zadejte kód součástky:")
amount = int(input("Zadejte počet:"))

if code in warehouse.keys():
    if amount > warehouse[code]:
        print("Lze prodat pouze omezené množství kusů.")
        del warehouse[code]
    else:
        print("Poptávku lze uspokojit v plné výši.")
        new_amount = warehouse[code] - amount
        warehouse[code] = new_amount
else:
    print("Není skladem")

print(warehouse)

