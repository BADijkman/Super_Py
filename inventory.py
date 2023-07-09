import csv
from console import console
from rich.table import Table
from rich.align import Align
from datetime import datetime
from matplot import pltShow
from handle_date import Date
from handle_cvs import Purchase


# displayInventory
def displayInventory(parsed_Data):
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
                count += 1
            else:
                item = Purchase.getItemById(int(line[0]))

                expiration_date = Date.convertToDateTime(
                    str(item['expiration_date']))
                buy_date = Date.convertToDateTime(str(item['buy_date']))
                check_date = Date.getDateFromFile("date")

                # checking expirate
                expirate_display = "[green]N0"
                if (expiration_date < check_date):
                    expirate_display = "[red]YES"

                # checking buy date
                if (buy_date > check_date):
                    pass
                else:
                    table.add_row(
                        line[1],
                        line[2],
                        "\u20ac " + item["buy_price"],
                        item['expiration_date'],
                        expirate_display
                    )

    display_date = Date.getDateFromFile("str")
    console.rule(f"[yellow]Inventory: {display_date}", style="yellow")
    console.print(Align.center(table))
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
    pltShow()
