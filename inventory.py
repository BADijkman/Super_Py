import csv
from console import console, err_console
from rich.table import Table
from rich.align import Align
from utils.utils import getItemFromBoughtCsvById
from datetime import datetime
from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from utils.reset_day_to_today import reset_date_to_today


# handleInventory
def handleInventory(parsed_Data):
    # today
    if parsed_Data.today:
        reset_date_to_today()
        date = getDateFromFile("str")
        displayInventory(date)
    # yesterday
    elif parsed_Data.yesterday:
        reset_date_to_today()
        # set date to yesterday
        date = getDateFromFile("date")
        with open("./day/day.txt", "w") as f:
            newDay = date + timedelta(days=-1)
            euDay = newDay.strftime("%d/%m/%Y")
            f.write(euDay)
        date_yesterday = getDateFromFile("str")
        displayInventory(date_yesterday)
    # now
    elif parsed_Data.now:
        date = getDateFromFile("str")
        displayInventory(date)
    # input date
    elif parsed_Data.date:
        date = datetime.strftime(parsed_Data.date, "%d/%m/%Y")
        with open("./day/day.txt", "w") as f:
            euDay = date
            f.write(euDay)
        displayInventory(date)
    else:
        err_console.print(
            'error :inventory needs argument -- now --today --yesterday  or date')


# displayInventory
def displayInventory(date):
    date = date
    table = Table(min_width=100, style='white',
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
                table.add_column("Expirtion date",
                                 justify="left",
                                 header_style="green",
                                 no_wrap=True,
                                 )
                table.add_column("Expirate",
                                 justify="left",
                                 header_style="green",
                                 no_wrap=True,
                                 )
                count += 1
            else:
                item = getItemFromBoughtCsvById(int(line[0]))

                # set expiration_date
                string_expiration_date = (
                    str(item['expiration_date']))
                expiration_date = datetime.strptime(
                    string_expiration_date, "%d/%m/%Y")

                # set buy_date
                string_buy_date = (
                    str(item['buy_date']))
                buy_date = datetime.strptime(
                    string_buy_date, "%d/%m/%Y")

                # set check_date
                check_date = getDateFromFile("date")

                # checking expirate
                if (expiration_date.date() < check_date):
                    display = "[red]YES"
                else:
                    display = "[green]N0"

                # checking buy date
                if (buy_date.date() > check_date):
                    pass
                else:
                    table.add_row(
                        item['product_name'],
                        item['amount'],
                        "\u20ac " + item["buy_price"],
                        item['expiration_date'],
                        display
                    )

    console.rule(f"[yellow]Inventory: {date}", style="yellow")
    console.print(Align.center(table))
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
