from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

converter = CurrencyRates()
amount = int(input("Zadejte požadovanou částku: "))
price_czk = converter.convert('EUR', 'CZK', amount)
print(f"Pro získání {amount} dolarů potřebujete {price_czk} CZK")


btc = BtcConverter()
amount_btc = int(input("Zadejte požadované množství BTC k převodu do CZK: "))
btc.get_latest_price('CZK')
price_czk_btc = btc.convert_to_btc(amount_btc, 'CZK')
print(f"Pro získání {amount_btc} bitcoinu potřebujete {price_czk_btc} CZK")
