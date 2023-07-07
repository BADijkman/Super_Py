-1 First, we check whether certain csv files already exist, and if not the will be created,
Also we put in the text file with the date, today’s date and if this text file does not exist we create it.

-------------------------------------------------------------------------
import os
import csv
from modify_day.date import get_date


def init_data(base_path, csv_path, day_path):
    # check cvs path
    if os.path.exists(csv_path):
        pass
    else:
        os.mkdir(f'{base_path}/csv')

    # check purchase.cvs excist
    if os.path.exists(f'{csv_path }/purchase.csv'):
        pass
    else:
        fieldnames = ['id', 'product_name', 'amount', 'buy_price',
                      'buy_date',  'expiration_date']
        with open(f'{csv_path }/purchase.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check sold.csv excist
    if os.path.exists(f'{csv_path}/sold.csv'):
        pass
    else:
        fieldnames = ['id', 'product_name', 'amount',
                      'sell_date', 'sell_price']

        with open(f'{csv_path }/sold.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check inventory.csv excist
    if os.path.exists(f'{csv_path }/inventory.csv'):
        pass
    else:
        fieldnames = ['id', 'name',
                      'amount', 'expiration_date']
        with open(f'{csv_path }/inventory.csv', 'w', encoding='UTF8', newline='')as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check day path
    if os.path.exists(day_path):
        pass
    else:
        os.mkdir(f'{base_path}/day')
        # set day to today
        with open("./day/day.txt", "w") as f:
            euDay = get_date()
            f.write(euDay)
-------------------------------------------------------------------------

-2 To check whether the products  are past their expiration date, you need to compare the expiration date with the current date.
The expiration date is taken from the csv file and is a string type
The current date is retrieved from the get date function and is  date time type

To compare you have to make the string type also a date time
So the expiration time needs to convert

-------------------------------------------------------------------------
from datetime import datetime

def convert_to_datetime(date_string):
    return datetime.strptime(date_string, "%d/%m/%Y")
-------------------------------------------------------------------------


when a date needs to be put back in the csv file it must be a string type again

-------------------------------------------------------------------------
def convert_to_string(date_object):
    return date_object.strftime("%d/%m/%Y")
-------------------------------------------------------------------------

-3 rich table is used to display the inventory in a table

First we make some columns add name and other specifications 

-------------------------------------------------------------------------
def displayInventory():
    table = Table(min_width=90, style='white',
                  header_style="green",
                  padding=(0, 2),
                  )
    with open("./csv/inventory.csv") as f:
        lines = csv.reader(f)
        count = 0
        for line in lines:
            if count == 0:
                table.add_column("Product Name",
                                 justify="left",
                                 no_wrap=True,
                                 )
                table.add_column("Amount",
                                 justify="left",
                                 no_wrap=True,
                                 )
                table.add_column("Purchase price",
                                 justify="left",
                                 no_wrap=True,
                                 )
                table.add_column("Expiration date",
                                 justify="left",
                                 header_style="green",
                                 no_wrap=True,
                                 )
                table.add_column("Expirate",
                                 justify="left",
                                 header_style="green",
                                 no_wrap=True,
                                 )
-------------------------------------------------------------------------


We check the expiration_date
-------------------------------------------------------------------------

if (expiration_date.date() < check_date):
                    display = "[red]YES"
                else:
                    display = "[green]N0"
-------------------------------------------------------------------------


We add the info taken from the inventory csv file
-------------------------------------------------------------------------
table.add_row(
                        line[1],
                        line[2],
                        "\u20ac " + item["buy_price"],
                        item['expiration_date'],
                        display
                    )
-------------------------------------------------------------------------

-4 To get only 1 bar for each product in the bar chart, the numbers must be added for several products of the same type.

-------------------------------------------------------------------------
def checkForDuplicateProducts(new_list):
    updated_list = []
    for dict in new_list:
        for key, value in dict.items():
            if key == "name":
                search_value = value
            elif key == "amount":
                input_Amount = value

        # If the search_value is found modify amount
        new_dict = True
        for dict in updated_list:
            if search_value in dict.values():
                amount = dict.get("amount")
                new_Amount = amount + input_Amount
                dict["amount"] = new_Amount
                new_dict = False
                break
        # If the search_value is not found, create a new dictionary
        if new_dict:
            new_dict = {"name": search_value, "amount": input_Amount}
            updated_list.append(new_dict)

    return (updated_list)
-------------------------------------------------------------------------
