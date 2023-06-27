import csv
from console import console, err_console
from rich.table import Table
from rich.align import Align
from utils.utils import getItemFromBoughtCsvById
from date import get_date
from datetime import datetime
from datetime import timedelta
from utils.getDateFromFile import getDateFromFile


# handleInventory
def handleInventory(parsed_Data):
    date = get_date()
    if parsed_Data.today:
        displayInventory(date)
    elif parsed_Data.yesterday:
        date = getDateFromFile("date")
        with open("./day/day.txt", "w") as f:
            newDay = date + timedelta(days=-1)
            euDay = newDay.strftime("%d/%m/%Y")
            f.write(euDay)
        date_yesterday = getDateFromFile("str")
        displayInventory(date_yesterday)
    else:
        err_console.print(
            'error :inventory needs argument --today or --yesterday ')


# displayInventory
def displayInventory(date):
    date = date
    table = Table(min_width=80, style='white',
                  header_style="green",
                  padding=(0, 2)
                  )
    with open("./csv/inventory.csv") as f:
        lines = csv.reader(f)
        count = 0
        for line in lines:
            if count == 0:
                table.add_column(
                    "Product Name",
                    justify="left",
                    no_wrap=True,

                )
                table.add_column("Amount",
                                 justify="left",
                                 no_wrap=True)
                table.add_column("Purchase price",
                                 justify="left",
                                 no_wrap=True)
                table.add_column("Expirtion date",
                                 justify="left",
                                 header_style="green",
                                 no_wrap=True
                                 )
                count += 1
            else:
                item = getItemFromBoughtCsvById(int(line[0]))
                string_input_with_date = (str(item['expiration_date']))
                past = datetime.strptime(string_input_with_date, "%d/%m/%Y")
                present_date = getDateFromFile("date")

                if (past.date() < present_date):
                    # expired = YES
                    pass
                else:
                    # expired = NO
                    table.add_row(
                        item['product_name'],
                        item['amount'],
                        "\u20ac " + item["buy_price"],
                        item['expiration_date']
                    )

    console.rule(f"[yellow]Inventory: {date}", style="yellow")
    console.print(Align.center(table))
