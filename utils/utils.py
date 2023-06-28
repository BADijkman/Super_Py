import csv
import os

base_path = os.getcwd()
csv_path = os.path.join(base_path, "csv")


# appendToBought
def appendToBoughtCsv(newId, name, price, amount, date, expiration_date):
    with open("./csv/bought.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([newId, name, amount,  price, date, expiration_date])


# appendToInventory
def appendToInventoryCsv(id, name, amount):
    with open("./csv/inventory.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([id, name, amount])


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


# appendToSold
def appendToSoldCsv(id, name, amount, date, price):
    with open("./csv/sold.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([id, name, amount, date, price])


# adjustInventory
def adjustInventoryCsv(id, amount):
    newLines = []
    with open("./csv/inventory.csv", "r+") as f:
        lines = csv.DictReader(f)
        for line in lines:
            if int(line["id"]) == id:
                newLines.append(
                    {
                        "id": line["id"],
                        "name": line["name"],
                        "amount": int(line["amount"]) - amount,
                    }
                )
            else:
                newLines.append(line)

    resetInventory()
    for line in newLines:
        appendToInventoryCsv(line["id"], line["name"], line["amount"])


# removeFromInventoryCsv(int(stock["id"]))
def removeFromInventoryCsv(id):
    newLines = []
    with open("./csv/inventory.csv") as f:
        lines = csv.DictReader(f)
        for line in lines:
            if int(line["id"]) != id:
                newLines.append(line)

    resetInventory()
    for line in newLines:
        appendToInventoryCsv(line["id"], line["name"], line["amount"])


def resetInventory():
    fieldnames = ['id', 'name',
                  'amount']
    with open(f'{csv_path }/inventory.csv', 'w', encoding='UTF8', newline='')as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()


# get item by id from bought
def getItemFromBoughtCsvById(id):
    with open("./csv/bought.csv") as f:
        lines = csv.DictReader(f)
        for line in lines:
            if int(line["id"]) == int(id):
                return line
