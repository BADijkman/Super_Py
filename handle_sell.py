from utils.utils import (getAllItemsByNameFromInventoryCsv,
                         appendToSoldCsv,
                         removeFromInventoryCsv,
                         adjustInventoryCsv,
                         sortOnDate
                         )
from functools import reduce
from console import console
from modify_day.date import get_date
from datetime import datetime


day = get_date()


def handleSell(parsed_Data, csv_path):
    name = parsed_Data.name.lower()
    price = parsed_Data.amount * parsed_Data.price
    amount = parsed_Data.amount
    sold = 0

    # sort on expiration_date
    sortOnDate("inventory")

    # Go through the inventory and get the product_name
    inStockTotal = getAllItemsByNameFromInventoryCsv(name)

    # select not expired
    inStockTotalNotExpired = []
    for dict in inStockTotal:
        expiration_date = datetime.strptime(
            dict['expiration_date'], "%d/%m/%Y")
        check_date = datetime.strptime(
            day, "%d/%m/%Y")
        if expiration_date < check_date:
            pass
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
                print(amount)
                print(inStockAmount)
               
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
