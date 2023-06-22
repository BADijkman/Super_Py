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
    print(inStock)

    # Check how much of the item is in stock.
    inStockAmount = reduce(
        lambda x, y: x + y, [d["amount"] for d in inStock], 0)
    print(f' er zijn {inStockAmount} {name} in stock')

    # Loop that handles the selling of the products.

    # while amount > 0:
    print(f'amount {amount}')
    if inStock:
        for stock in inStock:
            print("in stock ")
            print(stock['amount'])

            # the amount is higher than what is in stock
            if amount > stock["amount"] and inStockAmount != 0:
                print("ja")
                break
            elif inStockAmount == 0:
                print(f"You were only able to buy {sold}")
                amount = 0
                break
            else:
                print("pass")
                pass
    #     if amount == stock["amount"]:
    #         print(colored('OK', 'green',
    #               attrs=["reverse", 'bold']))
    # amount -= stock["amount"]
    # inStockAmount -= stock["amount"]
    # sold += stock["amount"]

    # remove the line from the inventory.csv and write the into sell.csv
    # appendRowToSoldCsv(
    #     stock["id"], name, stock["amount"], day, price)
    # removeLineFromInventoryCsv(int(stock["id"]))
    # continue

    # elif inStockAmount == 0:
    #     print(f"You were only able to buy {sold}")
    #     amount = 0
    #     break
    # else:
    #     appendRowToSoldCsv(stock["id"], name, amount, day, price)
    #     if amount == stock["amount"]:
    #         removeLineFromInventoryCsv(int(stock["id"]))
    #     else:
    #         adjustLineInInventoryCsv(int(stock["id"]), amount)
    #     # Set amount to 0 to reset the loop as the purchase has been fulfilled
    #     amount = 0
    #     sold += amount
    #     print(colored('OK', 'green',
    #                   attrs=["reverse", 'bold']))

    else:
        print(colored('ERROR: Product not in stock.', 'red'))
        #  break
