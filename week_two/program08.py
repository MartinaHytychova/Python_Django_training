import math

requested_number = input("Zadejte telefonní číslo, kam chcete zprávu poslat:")


def check_message_length(text):
    number = len(text) / 180
    amount = 3 * math.ceil(number)
    print(f"Za sms zaplatíte{amount} Kč.")


def check_phone_number(number):
    phone_number = number.replace(" ", "")
    if len(phone_number) == 9 or len(phone_number) == 13:
        check_message_length(input("Napište zprávu, kterou chcete odeslat:"))
        return True
    else:
        print("Nesprávný formát.")
        return False


check_phone_number(requested_number)
