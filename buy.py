
import random
from date import get_date
from termcolor import colored
from utils.utils import appendRowToBoughtCsv, appendRowToInventoryCsv


# import sys
# sys.path.insert(0, "../csv")
# # sys.path.insert(0, "../utils") #AD


def handleBuy(parsed_Data):
    newId = random.randint(1000000, 9999999)
    name = parsed_Data.name
    price = parsed_Data.price
    amount = parsed_Data.amount
    date = get_date()
    expiration_date = parsed_Data.expiration

    try:
        # Append line to bought.csv
        appendRowToBoughtCsv(newId, name, price, amount, date, expiration_date)

        # Append line to inventory.csv
        appendRowToInventoryCsv(newId, name, amount)

        print(colored('OK', 'green', attrs=["reverse", 'bold']))

    except:
        print(colored('an exception occurred', 'red'))
