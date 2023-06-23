
import csv
from csv import DictWriter


# appendToBought
def appendRowToBoughtCsv(newId, name, price, amount, date, expiration_date):
    dict = {'id': newId,
            'product_name': name,
            'amount': amount,
            'buy_date': date,
            'buy_price': price,
            'expiration_date': expiration_date}

    field_names = ['id',
                   'product_name',
                   'amount',
                   'buy_price',
                   'buy_date',
                   'expiration_date']

    with open('./csv/bought.csv', 'a')as f:
        dictwriter_object = DictWriter(
            f, fieldnames=field_names, delimiter=",")
        dictwriter_object.writerow(dict)
        f.close()


# appendToInventory
def appendRowToInventoryCsv(newId, name, amount):
    dict = {'id': newId,
            'product_name': name,
            'amount': amount,
            }

    field_names = ['id',
                   'product_name',
                   'amount',
                   ]

    with open('./csv/inventory.csv', 'a')as f:
        dictwriter_object = DictWriter(
            f, fieldnames=field_names, delimiter=",")
        dictwriter_object.writerow(dict)
        f.close()


# getAllItemsFromInventory
def getAllItemsByNameFromInventoryCsv(name):
    inStock = []
    with open('./csv/inventory.csv') as f:
        lines = csv.DictReader(f)
        for line in lines:
            if line["name"] == name:
                inStock.append(
                    {"id": int(line["id"]),
                        "name": line["name"],
                        "amount": int(line["amount"]), }
                )
    return inStock


def appendRowToSoldCsv(id, name, amount, sell_date, sell_price):
    dict = {'id': id,
            'name': name,
            'amount': amount,
            'sell_date': sell_date,
            'sell_price': sell_price
            }
    field_names = ['id',
                   'name',
                   'amount',
                   'sell_date',
                   'sell_price',
                   ]

    with open('./cvs/sold.csv', 'a')as f:
        dictwriter_object = DictWriter(
            f, fieldnames=field_names, delimiter=",")
        dictwriter_object.writerow(dict)
        f.close()


# removeLineFromInventoryCsv(int(stock["id"]))
def resetInventory():
    with open("./csv/inventory.csv", "w") as inv:
        writer = csv.writer(inv, lineterminator="")
        writer.writerow(["id", "name", "amount"])


def removeLineFromInventoryCsv(inputId):
    newLines = []
    with open("./csv/inventory.csv") as f:
        lines = csv.DictReader(f)
        for line in lines:
            if int(line["id"]) != inputId:
                newLines.append(line)

    resetInventory()
    for line in newLines:
        appendRowToInventoryCsv(line["id"], line["name"], line["amount"])
