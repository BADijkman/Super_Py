import random
# from modify_day.date import get_date
from utils.utils import appendToPurchaseCsv, appendToInventoryCsv
from console import console
from modify_day.setDate import Date


def handleBuy(parsed_Data):
    newId = random.randint(1000000, 9999999)
    name = parsed_Data.name
    price = round(parsed_Data.amount * parsed_Data.price, 2)
    amount = parsed_Data.amount
    date = Date.get_date()
    expiration_date = parsed_Data.expiration.strftime("%d/%m/%Y")

    try:
        # Append line to purchase.csv
        appendToPurchaseCsv(newId, name, price, amount, date, expiration_date)

        # Append line to inventory.csv
        appendToInventoryCsv(newId, name, amount, expiration_date)
        console.print("[green bold reverse]OK")

    except ValueError:
        console.print("[red bold reverse]an exception occurred")
