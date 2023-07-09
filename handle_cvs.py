import csv
import operator
from datetime import datetime
# from modify_day.convert_to_datetime import convert_to_datetime
# from modify_day.convert_to_string import convert_to_string
# from modify_day.date import get_date
from handle_date import Date
day = Date.get_date()


class Purchase():

    def appendToCsv(newId, name, price, amount, date, expiration_date):
        with open("./csv/purchase.csv", "a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(
                [newId, name, amount,  price, date, expiration_date])

    def getItemById(id):
        with open("./csv/purchase.csv") as f:
            lines = csv.DictReader(f)
            for line in lines:
                if int(line["id"]) == int(id):
                    return line

    def getAllItemsByDate(date, parsed_data):
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


class Inventory():
    def appendToCsv(id, name, amount, buy_date, expiration_date):
        with open("./csv/inventory.csv", "a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([id, name, amount, buy_date, expiration_date])
        Inventory.sortOnDate("inventory")

    def getAllItemsByNameFromCsv(name):
        inStock = []
        with open('./csv/inventory.csv') as f:
            lines = csv.DictReader(f)
            for line in lines:
                if line["name"] == name:
                    inStock.append(
                        {"id": int(line["id"]),
                            "name": line["name"],
                            "amount": int(line["amount"]),
                            "buy_date": str(line["buy_date"]),
                            "expiration_date": str(line["expiration_date"])}
                    )
        Inventory.sortOnDate("inventory")
        return inStock

    def reset(csv_path):
        fieldnames = ['id', 'name',
                      'amount', 'expiration_date']
        with open(f'{csv_path}/inventory.csv', 'w', encoding='UTF8', newline='')as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()
        Inventory.sortOnDate("inventory")

    def removeFromCsv(id, csv_path):
        newLines = []
        with open("./csv/inventory.csv") as f:
            lines = csv.DictReader(f)
            for line in lines:
                if int(line["id"]) != id:
                    newLines.append(line)

        Inventory.reset(csv_path)
        for line in newLines:
            Inventory.appendToCsv(line["id"], line["name"],
                                  line["amount"], line["expiration_date"])

    def adjustCsv(id, amount, csv_path):
        Inventory.sortOnDate("inventory")
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
                            "buy_date": str(line["buy_date"]),
                            "expiration_date": line["expiration_date"]
                        }
                    )
                else:
                    newLines.append(line)

        Inventory.reset(csv_path)
        for line in newLines:
            Inventory.appendToCsv(line["id"], line["name"],
                                  line["amount"], line["buy_date"], line["expiration_date"])

    def total():
        inStock = []
        with open('./csv/inventory.csv') as f:
            lines = csv.DictReader(f)
            for line in lines:
                check_date = Date.getDateFromFile("date")
                buy_date = Date.convertToDateTime(str(line['buy_date']))
                if (buy_date > check_date):
                    pass
                else:
                    inStock.append(
                        {"id": int(line["id"]),
                         "name": line["name"],
                         "amount": int(line["amount"]),
                         "buy_date": str(line["buy_date"]),
                         "expiration_date": str(line["expiration_date"])}
                    )
        Inventory.sortOnDate("inventory")
        return inStock

    def totalNotExpired(inStock):
        inStockTotalNotExpired = []
        for dict in inStock:
            expiration_date = datetime.strptime(
                dict['expiration_date'], "%d/%m/%Y")
            check_date = datetime.strptime(
                day, "%d/%m/%Y")
            if expiration_date < check_date:
                pass
            else:
                inStockTotalNotExpired.append(dict)
        return inStockTotalNotExpired

    def sortOnDate(key):
        data = []
        if key == "inventory":
            with open('./csv/inventory.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert the value in the date column to a datetime object
                    row['expiration_date'] = Date.convertToDateTime(
                        row['expiration_date'])
                    data.append(row)

        key = 'expiration_date'
        # Sort the data list
        sorted_data = sorted(data, key=operator.itemgetter(key))

        # Convert datetime objects back to string format
        for row in sorted_data:
            row['expiration_date'] = Date.convertToString(
                row['expiration_date'])

        # Write the sorted data back to a CSV file
        with open('./csv/inventory.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(sorted_data)


class Sold():
    def appendToCsv(id, name, amount, date, price):
        with open("./csv/sold.csv", "a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([id, name, amount, date, price])

    def getAllItemsByDate(date, parsed_data):
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
