
-1 Init
First, we check whether certain csv files already exist, and if not the will be created, we also set the current_date text file on today

def init_data(base_path, csv_path, day_path): # check cvs path
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
etc etc



-2 compare dates

To check whether the products are past their expiration date, you need to compare the expiration date with the current date.
The expiration date is taken from the csv file and is a string type
The current date is retrieved from the get date function and is date time type

To compare you have to make the string type also a date time
So the expiration time needs to convert

def convertToString(date_object):
        return date_object.strftime("%d/%m/%Y")

    def convertToDateTime(date_string):
        datetime_obj = datetime.strptime(date_string, "%d/%m/%Y")
        return datetime_obj.date()


-3 modify date

To adjust the date we make it a text file, we call it up, we adjust it and put it back in the text file using timedelta

def advance_date(delta_time):
        with open("./current_date/current_date.txt", 'r') as f:
            line = "".join(f.readline().split("/"))
            date = datetime.strptime(line, "%d%m%Y").date()
            newDate = date + timedelta(days=delta_time)
            newDate = newDate.strftime("%d/%m/%Y")
            with open("./current_date/current_date.txt", 'w') as f:
                f.write(newDate)
            console.print(f"[green]Current day set to: {newDate}")


-4 rich table is used to display the inventory in a table

First we make some columns for the header, add name and other specifications,

def displayInventory(parsed_data):
    table = Table(min_width=90, style='white',
                  header_style="green",
                  padding=(0, 2),
                  )
    table.add_column("Product Name",
                     justify="left",
                     no_wrap=True,
                     )
    table.add_column("Amount",
                     justify="left",
                     no_wrap=True,
                     )
    etc, etc

the argument parsed_date is not used but in a later stadion we
we can use it, maybe to decide to show yes or now the bar chart


with function Inventory.total()
we get a list of dicts from the total inventory
now we iterate over this dicts to get name price expire_date etc

we can check the expire_date 

and add a row to the table with selected name price and date,

 inventory = Inventory.total()

    for product in inventory:

        check_date = Date.getDateFromFile("date")
        expiration_date = Date.convertToDateTime(
            product['expiration_date'])

        # checking expirate
        expirate_display = "[green]N0"
        if (expiration_date < check_date):
            expirate_display = "[red]YES"

        table.add_row(
            product['name'],
            str((product['amount'])),
            "\u20ac " + str((product['buy_price'])),
            product['expiration_date'],
            expirate_display


-5 matplot is uses to get a bar chart from the inventory

To get only 1 bar for each product in the bar chart, the numbers must be added for several products of the same type.

def checkForDuplicateProducts(list):
    updated_list = []
    for dict in list:
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