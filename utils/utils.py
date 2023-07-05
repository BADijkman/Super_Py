import csv
import operator
from datetime import datetime
from modify_day.convert_to_datetime import convert_to_datetime
from modify_day.convert_to_string import convert_to_string


# sort on date
def sortOnDate(cvs):
    data = []
    if cvs == "inventory":
        with open('./csv/inventory.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert the value in the date column to a datetime object
                row['expiration_date'] = convert_to_datetime(
                    row['expiration_date'])
                data.append(row)

    key = 'expiration_date'
    # Sort the data list 
    sorted_data = sorted(data, key=operator.itemgetter(key))

    # Convert datetime objects back to string format
    for row in sorted_data:
        # Replace 'date_column' with your actual column name
        row['expiration_date'] = convert_to_string(row['expiration_date'])

    # Write the sorted data back to a CSV file
    with open('./csv/inventory.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(sorted_data)


# appendToPurchase
def appendToPurchaseCsv(newId, name, price, amount, date, expiration_date):
    with open("./csv/purchase.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([newId, name, amount,  price, date, expiration_date])


# appendToInventory
def appendToInventoryCsv(id, name, amount, expiration_date):
    with open("./csv/inventory.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([id, name, amount, expiration_date])
    sortOnDate("inventory")


# appendToSold
def appendToSoldCsv(id, name, amount, date, price):
    with open("./csv/sold.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([id, name, amount, date, price])


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
    sortOnDate("inventory")
    return inStock


# resetInventory
def resetInventory(csv_path):
    fieldnames = ['id', 'name',
                  'amount', 'expiration_date']
    with open(f'{csv_path}/inventory.csv', 'w', encoding='UTF8', newline='')as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()
    sortOnDate("inventory")


# adjustInventory
def adjustInventoryCsv(id, amount, csv_path):
    sortOnDate("inventory")
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
                        "expiration_date": line["expiration_date"]
                    }
                )
            else:
                newLines.append(line)

    resetInventory(csv_path)
    for line in newLines:
        appendToInventoryCsv(line["id"], line["name"],
                             line["amount"], line["expiration_date"])


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
        appendToInventoryCsv(line["id"], line["name"],
                             line["amount"], line["expiration_date"])


# get item by id from Purchase
def getItemFromPurchaseCsvById(id):
    with open("./csv/purchase.csv") as f:
        lines = csv.DictReader(f)
        for line in lines:
            if int(line["id"]) == int(id):
                return line


# get all items sold by date
def getAllItemsSoldByDate(date, parsed_data):
    with open("./csv/sold.csv", 'r') as f:
        sold = []
        lines = csv.DictReader(f)
        check_date = datetime.strptime(
            date, "%d/%m/%Y")
        if parsed_data.startingdate is None:
            for line in lines:
                sell_date = datetime.strptime(
                    line["sell_date"], "%d/%m/%Y")
                if check_date == sell_date:
                    sold.append(float(line["sell_price"]))
        elif parsed_data.startingdate is not None:
            for line in lines:
                sell_date = datetime.strptime(
                    line["sell_date"], "%d/%m/%Y")
                if check_date <= sell_date:
                    sold.append(float(line["sell_price"]))
    return sum(sold)


# get all items purchase by date
def getAllItemsPurchaseByDate(date, parsed_data):
    with open("./csv/purchase.csv", 'r') as f:
        purchase = []
        lines = csv.DictReader(f)
        check_date = datetime.strptime(
            date, "%d/%m/%Y")
        if parsed_data.startingdate is None:
            for line in lines:
                purchase_date = datetime.strptime(
                    line["buy_date"], "%d/%m/%Y")
                if check_date == purchase_date:
                    purchase.append(float(line["buy_price"]))
        elif parsed_data.startingdate is not None:
            for line in lines:
                purchase_date = datetime.strptime(
                    line["buy_date"], "%d/%m/%Y")
                if check_date <= purchase_date:
                    purchase.append(float(line["buy_price"]))
    return sum(purchase)
