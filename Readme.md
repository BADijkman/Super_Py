




-3 rich table is used to display the inventory in a table

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







#-----------------------
-4 matplot is uses to get a bar chart from the inventory

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