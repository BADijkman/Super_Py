import csv
# import os


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
def adjustInventoryCsv(id, amount, csv_path):
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

    resetInventory(csv_path)
    for line in newLines:
        appendToInventoryCsv(line["id"], line["name"], line["amount"])


# removeFromInventoryCsv(int(stock["id"]))
def removeFromInventoryCsv(id, csv_path):
    newLines = []
    with open("./csv/inventory.csv") as f:
        lines = csv.DictReader(f)
        for line in lines:
            if int(line["id"]) != id:
                newLines.append(line)

    resetInventory(csv_path)
    for line in newLines:
        appendToInventoryCsv(line["id"], line["name"], line["amount"])


def resetInventory(csv_path):
    fieldnames = ['id', 'name',
                  'amount']
    with open(f'{csv_path}/inventory.csv', 'w', encoding='UTF8', newline='')as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()


# get item by id from bought
def getItemFromBoughtCsvById(id):
    with open("./csv/bought.csv") as f:
        lines = csv.DictReader(f)
        for line in lines:
            if int(line["id"]) == int(id):
                return line

# get all items sold by date


def getAllItemsSoldByDate(date):
    with open("./csv/sold.csv", 'r') as f:
        sold = []
        lines = csv.DictReader(f)
        search_value = "02/07/2024"
        print(search_value)
        for line in lines:
            if search_value >= line["sell_date"]:
                print("true")
                sold.append(float(line["sell_price"]))
    return sold
## datum veranderen naar date

# for row in reader:
#     if search_value in row:
#         return True
# def getAllItemsSoldByDate(inputDate):
#     print(inputDate)
#     sold = []
#     with open("./csv/sold.csv") as f:
#         lines = csv.DictReader(f)
#         for line in lines:
#             print(line)

    # if inputDate in line["sell_date"]:
    #     sold.append(line)
    #     continue
    # return sold
