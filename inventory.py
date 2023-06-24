import csv
from console import console
from rich.table import Table
from rich.align import Align
from utils.utils import getItemFromBoughtCsvById
from date import get_date


date = get_date()
# from utils.utils import getItemFromBoughtCsvById
# from utils.getDateFromFile import getDateFromFile


def displayCurrentInventory():
    day = get_date()
    table = Table(min_width=80, style='white',
                  header_style="green",
                  padding=0)
    with open("./csv/inventory.csv") as f:
        lines = csv.reader(f)
        count = 0
        for line in lines:
            if count == 0:
                table.add_column(
                    "Product Name",
                    justify="left",
                    no_wrap=True)
                table.add_column("Amount",
                                 justify="left",
                                 no_wrap=True)
                table.add_column("Purchase price",
                                 justify="left",
                                 no_wrap=True)
                table.add_column("Expiration", justify="left",
                                 header_style="green",
                                 no_wrap=True
                                 )
                table.add_column("Expired", justify="left",
                                 header_style="green",
                                 no_wrap=True
                                 )
                count += 1
            else:

                item = getItemFromBoughtCsvById(int(line[0]))

                # print(str(item['expiration_date']) < str(date))

                if item['expiration_date'] < (date):
                    expired = "YES"
                else:
                    expired = "NO"
                # expired = "YES"
                table.add_row(
                    item['product_name'],
                    item['amount'],
                    "\u20ac " + item["buy_price"],
                    item["expiration_date"],
                    expired
                )

    console.rule(f"[yellow]Inventory: {day}", style="yellow")
    console.print(Align.center(table))


# displaydisplayCurrentInventory
