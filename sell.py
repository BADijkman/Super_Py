from utils.utils import getAllItemsByNameFromInventoryCsv
from functools import reduce


def handleSell(parsed_Data):
    name = parsed_Data.name.lower()
    price = parsed_Data.price
    amount = parsed_Data.amount
    sold = 0
    pass

    # Go through the inventory and get the product_name
    inStock = getAllItemsByNameFromInventoryCsv(name)
    print(f'in stock van gekozen te verkopen pruduct {inStock}')

    # Check how much of the item is in stock.
    inStockAmount = reduce(
        lambda x, y: x + y, [d["amount"] for d in inStock], 0)
    print(f' er zijn {inStockAmount} {name} in stock')
