packages = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

package_number = input("Prosím zadejte kód vaší zásilky:")

if package_number in packages:
    print("Balík byl předán kurýrovi.")
else:
    print("Balík zatím nebyl předán kurýrovi.")
