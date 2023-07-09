from functools import reduce
from console import console
from datetime import datetime
from handle_date import Date
from handle_cvs import Sold, Inventory


day = Date.get_date()


def handleSell(parsed_Data, csv_path):
    name = parsed_Data.name.lower()
    price = round(parsed_Data.amount * parsed_Data.price, 2)
    amount = parsed_Data.amount
    sold = 0

    # sort on expiration_date
    Inventory.sortOnDate("inventory")

    # Go through the inventory and get the product_name
    inStockTotal = Inventory.getAllItemsByNameFromCsv(name)

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
                if amount > inStockAmount:
                    console.print(
                        f' [red bold reverse] ERROR:You can only sell {inStockAmount} {name}'
                        )
                    amount = 0
                    break
                elif amount > stock["amount"] and inStockAmount != 0:
                    if amount == stock["amount"]:
                        console.print("[green bold reverse]OK")
                    amount -= stock["amount"]
                    inStockAmount -= stock["amount"]
                    sold += stock["amount"]
                    Sold.appendToCsv(
                        stock["id"], name, stock["amount"], day, price)
                    Inventory.removeFromCsv(int(stock["id"]), csv_path)
                    continue

                else:
                    Sold.appendToCsv(
                        stock["id"], name, amount, day, price)
                    if amount == stock["amount"]:
                        Inventory.removeFromCsv(int(stock["id"]), csv_path)
                    else:
                        Inventory.adjustCsv(int(stock["id"]), amount, csv_path)
                    # Set amount to 0 to reset the loop
                    amount = 0
                    sold += amount
                    console.print("[green bold reverse]OK")
                    break
        else:
            console.print("[red bold reverse]ERROR: Product not in stock.")
            break
