import csv
from console import console
from rich.table import Table
from rich.align import Align
from utils.utils import getItemFromPurchaseCsvById
from modify_day.getDateFromFile import getDateFromFile
from datetime import datetime


# displayInventory
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
                item = getItemFromPurchaseCsvById(int(line[0]))

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
                        line[1],
                        line[2],
                        "\u20ac " + item["buy_price"],
                        item['expiration_date'],
                        display
                    )

    display_date = getDateFromFile("str")
    console.rule(f"[yellow]Inventory: {display_date}", style="yellow")
    console.print(Align.center(table))
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
