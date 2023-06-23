from utils.utils import (getAllItemsByNameFromInventoryCsv,
                         appendRowToSoldCsv,
                         removeLineFromInventoryCsv
                         )
from functools import reduce
from termcolor import colored
from date import get_date


day = get_date()


def handleSell(parsed_Data):
    name = parsed_Data.name.lower()
    price = parsed_Data.price
    amount = parsed_Data.amount
    sold = 0
    pass

    # Go through the inventory and get the product_name
    inStock = getAllItemsByNameFromInventoryCsv(name)

    # Check how much of the item is in stock.
    inStockAmount = reduce(
        lambda x, y: x + y, [d["amount"] for d in inStock], 0)

    # Loop that handles the selling of the products.

    print(f' parsed aantal om verkocht te worden {amount}')
    print(f' er zijn {inStockAmount} {name} in stock')
    print(inStock)
    print (if instock: )

   