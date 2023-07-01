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
from revenue import displayRevenue
from profit import displayProfit


def handleReport(parsed_Data):
    print(parsed_Data)
    if hasattr(parsed_Data, 'inventory'):
        if parsed_Data.inventory:
            if parsed_Data.today:
                set_day_to_today()
                date = getDateFromFile("str")
                displayInventory(date)
            elif parsed_Data.yesterday:
                set_day_to_today()
                set_day_to_yesterday()
                date_yesterday = getDateFromFile("str")
                displayInventory(date_yesterday)
            elif parsed_Data.now:
                date_now = getDateFromFile("str")
                displayInventory(date_now)
            elif parsed_Data.date:
                set_day_to_inputday(parsed_Data)
                date_input = getDateFromFile("str")
                displayInventory(date_input)

    elif hasattr(parsed_Data, 'profit'):
        if parsed_Data.profit:
            if parsed_Data.today:
                set_day_to_today()
                date = getDateFromFile("str")
                displayProfit(date)
            elif parsed_Data.yesterday:
                set_day_to_today()
                set_day_to_yesterday()
                date_yesterday = getDateFromFile("str")
                displayProfit(date_yesterday)
            elif parsed_Data.now:
                date_now = getDateFromFile("str")
                displayProfit(date_now)
            elif parsed_Data.date:
                set_day_to_inputday(parsed_Data)
                date_input = getDateFromFile("str")
                displayProfit(date_input)

    elif hasattr(parsed_Data, 'revenue'):
        if parsed_Data.revenue:
            if parsed_Data.today:
                set_day_to_today()
                date = getDateFromFile("str")
                displayRevenue(date)
            elif parsed_Data.yesterday:
                set_day_to_today()
                set_day_to_yesterday()
                date_yesterday = getDateFromFile("str")
                displayRevenue(date_yesterday)
            elif parsed_Data.now:
                date_now = getDateFromFile("str")
                displayRevenue(date_now)
            elif parsed_Data.date:
                set_day_to_inputday(parsed_Data)
                date_input = getDateFromFile("str")
                displayRevenue(date_input)

    else:
        err_console.print(
            'error :inventory needs argument --now --today --yesterday or --date')
