
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

    with open('./cvs/bought.csv', 'a')as f:
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

    with open('./cvs/inventory.csv', 'a')as f:
        dictwriter_object = DictWriter(
            f, fieldnames=field_names, delimiter=",")
        dictwriter_object.writerow(dict)
        f.close()


# getAllItemsFromInventory
def getAllItemsByNameFromInventoryCsv(name):
    inStock = []
    with open('./cvs/inventory.csv') as f:
        lines = csv.DictReader(f)
        for line in lines:
            if line["name"] == name:
                inStock.append(
                    {"id": int(line["id"]),
                        "name": line["name"],
                        "amount": int(line["amount"]), }
                )
    return inStock
