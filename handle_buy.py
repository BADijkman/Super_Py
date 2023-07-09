import random
# from modify_day.date import get_date
# from handle_cvs import appendToPurchaseCsv, appendToInventoryCsv
# from handle_cvs import appendToInventoryCsv
from console import console
from handle_date import Date
from handle_cvs import Purchase, Inventory


def handleBuy(parsed_Data):
    newId = random.randint(1000000, 9999999)
    name = parsed_Data.name
    price = round(parsed_Data.amount * parsed_Data.price, 2)
    amount = parsed_Data.amount
    date = Date.get_date()
    expiration_date = parsed_Data.expiration.strftime("%d/%m/%Y")

    try:
        # Append line to purchase.csv
        Purchase.appendToCsv(newId, name, price, amount, date, expiration_date)

        # Append line to inventory.csv
        Inventory.appendToCsv(newId, name, amount,  date, expiration_date)
        console.print("[green bold reverse]OK")

    except ValueError:
        console.print("[red bold reverse]an exception occurred")
