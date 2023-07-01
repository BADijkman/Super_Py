# import csv
from console import console, err_console
# from rich.table import Table
# from rich.align import Align
# from utils.utils import getItemFromBoughtCsvById
# from datetime import datetime

from modify_day.getDateFromFile import getDateFromFile
from modify_day.set_day_to_today import set_day_to_today
from modify_day.set_day_to_yesterday import set_day_to_yesterday
from modify_day.set_day_to_inputday import set_day_to_inputday
from inventory import displayInventory
# from revenue import displayRevenue
# from profit import displayProfit


def handleReport(parsed_Data):
    print(parsed_Data)
    # today
    if parsed_Data.today:
        set_day_to_today()
        date = getDateFromFile("str")
        if parsed_Data.inventory:
            # print(f"Inventory {date}")
            displayInventory(date)
        elif parsed_Data.profit:
            # print(f"Profit {date}")
            displayInventory(date)
        elif parsed_Data.revenue:
            # print(f"Revenue {date}")
            displayInventory(date)

    # yesterday
    elif parsed_Data.yesterday:
        set_day_to_today()
        set_day_to_yesterday()
        date_yesterday = getDateFromFile("str")
        if parsed_Data.inventory:
            # print(f"Inventory {date_yesterday}")
            displayInventory(date_yesterday)
        elif parsed_Data.profit:
            # print(f"Profit {date_yesterday}")
            displayInventory(date_yesterday)
        elif parsed_Data.revenue:
            # print(f"Revenue {date_yesterday}")
            displayInventory(date_yesterday)

    # now
    elif parsed_Data.now:
        date_now = getDateFromFile("str")
        if parsed_Data.inventory:
            print(f"Inventory {date_now}")
            displayInventory(date_now)
        elif parsed_Data.profit:
            print(f"Profit {date_now}")
            displayInventory(date_now)
        elif parsed_Data.revenue:
            print(f"Revenue {date_now}")
            displayInventory(date_now)

    # input date
    elif parsed_Data.date:
        set_day_to_inputday(parsed_Data)
        date_input = getDateFromFile("str")
        if parsed_Data.inventory:
            # print(f"Inventory { date_input}")
            displayInventory(date_input)
        elif parsed_Data.profit:
            # print(f"Profit {date_input}")
            displayInventory(date_now)
        elif parsed_Data.revenue:
            # print(f"Revenue {date_input}")
            displayInventory(date_input)

    else:
        err_console.print(
            'error :inventory needs argument -- now --today --yesterday or date')
