
from console import console
from rich.table import Table
from rich.align import Align
from datetime import datetime
from matplot import pltShow
from handle_date import Date
from handle_cvs import Inventory


# displayInventory
def displayInventory(parsed_Data):
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
        )

    display_date = Date.getDateFromFile("str")

    console.rule(f"[yellow]Inventory: {display_date}", style="yellow")
    console.print(Align.center(table))
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
    pltShow()
