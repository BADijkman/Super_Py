import random
from date import get_date
from utils.utils import appendToBoughtCsv, appendToInventoryCsv
from console import console


def handleBuy(parsed_Data):
    newId = random.randint(1000000, 9999999)
    name = parsed_Data.name
    price = parsed_Data.price
    amount = parsed_Data.amount
    date = get_date()
    expiration_date = parsed_Data.expiration.strftime("%d/%m/%Y")

    try:
        # Append line to bought.csv
        appendToBoughtCsv(newId, name, price, amount, date, expiration_date)

        # Append line to inventory.csv
        appendToInventoryCsv(newId, name, amount)
        console.print("[green bold reverse]OK")

    except:
        console.print("[red bold reverse]an exception occurred")
