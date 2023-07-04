from utils.utils import (getAllItemsByNameFromInventoryCsv,
                         appendToSoldCsv,
                         removeFromInventoryCsv,
                         adjustInventoryCsv,
                         getItemFromPurchaseCsvById
                         )
from functools import reduce
from console import console
from date import get_date
from datetime import datetime


day = get_date()


def handleSell(parsed_Data, csv_path):
    print(parsed_Data)
    name = parsed_Data.name.lower()
    price = parsed_Data.price
    amount = parsed_Data.amount
    sold = 0

    # Go through the inventory and get the product_name
    inStockTotal = getAllItemsByNameFromInventoryCsv(name)
    print(f'instock total{inStockTotal}')

    # get these items from purchase by id to check Expirtion date
    inStockTotalNotExpired = []
    for dict in inStockTotal:
        id_inStockTotal = dict['id']

        inStockTotalById = getItemFromPurchaseCsvById(id_inStockTotal)

        for key, value in inStockTotalById.items():
            if key == 'expiration_date':
                expiration_date = datetime.strptime(
                    value, "%d/%m/%Y")
                check_date = datetime.strptime(
                    day, "%d/%m/%Y")
                print(f'e {expiration_date}')
                print(f'c {check_date}')
                if expiration_date < check_date:
                    print("YES")
                else:
                    inStockTotalNotExpired.append(dict)

    # Check how much of the item is in stock.
    inStock = inStockTotalNotExpired
    inStockAmount = reduce(
        lambda x, y: x + y, [d["amount"] for d in inStock], 0)

    # Loop that handles the selling of the products.
    while amount > 0:
        if inStock:
            for stock in inStock:
                if amount > inStockAmount:
                    console.print(
                        f' [red bold reverse] ERROR:You can only sell {inStockAmount} {name}')
                    amount = 0
                    break
                elif amount > stock["amount"] and inStockAmount != 0:
                    if amount == stock["amount"]:
                        console.print("[green bold reverse]OK")
                        amount -= stock["amount"]
                    inStockAmount -= stock["amount"]
                    sold += stock["amount"]
                    appendToSoldCsv(
                        stock["id"], name, stock["amount"], day, price)
                    removeFromInventoryCsv(int(stock["id"]), csv_path)
                    continue
                else:
                    appendToSoldCsv(
                        stock["id"], name, amount, day, price)
                    if amount == stock["amount"]:
                        removeFromInventoryCsv(int(stock["id"]), csv_path)
                    else:
                        adjustInventoryCsv(int(stock["id"]), amount, csv_path)
                    # Set amount to 0 to reset the loop
                    amount = 0
                    sold += amount
                    console.print("[green bold reverse]OK")
                    break
        else:
            console.print("[red bold reverse]ERROR: Product not in stock.")
            break
