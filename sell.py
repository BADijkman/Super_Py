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

    while amount > 0:
        if inStock:
            for stock in inStock:
                if amount > stock["amount"] and inStockAmount != 0:
                    if amount == stock["amount"]:
                        print(colored('OK', 'green',
                              attrs=["reverse", 'bold']))
                        amount -= stock["amount"]
                    inStockAmount -= stock["amount"]
                    sold += stock["amount"]
                    print("functie om rij aan sold cvs toe te voegen")
                    appendRowToSoldCsv(
                        stock["id"], name, stock["amount"], day, price)

                    print("functie om rij uit voorraad cvs toe te halen")
                    removeLineFromInventoryCsv(int(stock["id"]))
                    continue
                elif inStockAmount == 0:
                    print(f"You were only able to buy {sold}")
                    amount = 0
                    break
                else:
                    print("functie om rij aan sold cvs toe te voegen")
                    appendRowToSoldCsv(
                        stock["id"], name, amount, day, price)
                    if amount == stock["amount"]:
                        print("functie02 removeLineFromInventoryCsv")
                        removeLineFromInventoryCsv(int(stock["id"]))

                    else:
                        print("functie03 adjustLineInInventoryCsv")
                        # adjustLineInInventoryCsv(int(stock["id"]), amount)

                    # Set amount to 0 to reset the loop as the purchase has been fulfilled
                    amount = 0
                    sold += amount
                    print(colored('OK', 'green', attrs=["reverse", 'bold']))
                    break
        else:
            print(colored('ERROR: Product not in stock.', 'red'))
            break
