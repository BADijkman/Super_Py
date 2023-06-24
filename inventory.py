import csv
from console import console
from rich.table import Table
from rich.align import Align
from utils.utils import getItemFromBoughtCsvById
from date import get_date
from datetime import datetime


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
                    justify="center",
                    no_wrap=True)
                table.add_column("Amount",
                                 justify="center",
                                 no_wrap=True)
                table.add_column("Purchase price",
                                 justify="center",
                                 no_wrap=True)
                table.add_column("Expirtion date", justify="center",
                                 header_style="green",
                                 no_wrap=True
                                 )
                table.add_column("Expired", justify="center",
                                 header_style="green",
                                 no_wrap=True
                                 )
                count += 1
            else:

                item = getItemFromBoughtCsvById(int(line[0]))

                string_input_with_date = (str(item['expiration_date']))
                past = datetime.strptime(string_input_with_date, "%d/%m/%Y")
                present = datetime.now()
                if (past.date() < present.date()):
                    expired = "YES"
                else:
                    expired = "NO"

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
