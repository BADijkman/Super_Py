from console import err_console
from inventory import displayInventory
from revenue import displayRevenue
from profit import displayProfit
from datetime import datetime
from handle_date import Date


def handleReport(parsed_Data):
    if hasattr(parsed_Data, 'inventory'):
        if parsed_Data.inventory:
            if parsed_Data.today:
                Date.today()
                displayInventory(parsed_Data)
            elif parsed_Data.yesterday:
                Date.today()
                Date.yesterday()
                displayInventory(parsed_Data)
            elif parsed_Data.now:
                displayInventory(parsed_Data)
            elif parsed_Data.date:
                Date.input_date(parsed_Data)
                displayInventory(parsed_Data)
            else:
                err_console.print('error :inventory needs argument: --today ' /
                                  '--yesterday --now --date --startingdate')

    elif hasattr(parsed_Data, 'profit'):
        if parsed_Data.profit:
            if parsed_Data.today:
                Date.today()
                displayProfit(parsed_Data)
            elif parsed_Data.yesterday:
                Date.today()
                Date.yesterday()
                displayProfit(parsed_Data)
            elif parsed_Data.now:
                displayProfit(parsed_Data)
            elif parsed_Data.date:
                Date.input_date(parsed_Data)
                displayProfit(parsed_Data)
            elif parsed_Data.startingdate:
                check_date = datetime.strptime(Date.get_date(), "%d/%m/%Y")
                if parsed_Data.startingdate > check_date:
                    err_console.print("entry date past current date")
                else:
                    Date.starting_date(parsed_Data)
                    displayProfit(parsed_Data)
            else:
                err_console.print('error :inventory needs argument: --today ' /
                                  '--yesterday --now --date --startingdate')

    elif hasattr(parsed_Data, 'revenue'):
        if parsed_Data.revenue:
            if parsed_Data.today:
                Date.today()
                displayRevenue(parsed_Data)
            elif parsed_Data.yesterday:
                Date.today()
                Date.yesterday()
                displayRevenue(parsed_Data)
            elif parsed_Data.now:
                displayRevenue(parsed_Data)
            elif parsed_Data.date:
                Date.input_date(parsed_Data)
                displayRevenue(parsed_Data)
            elif parsed_Data.startingdate:
                check_date = datetime.strptime(Date.get_date(), "%d/%m/%Y")
                if parsed_Data.startingdate > check_date:
                    err_console.print("entry date past current date")
                else:
                    Date.starting_date(parsed_Data)
                    displayRevenue(parsed_Data)
            else:
                err_console.print('error :inventory needs argument: --today ' /
                                  '--yesterday --now --date --startingdate')

    else:
        err_console.print(
            'error :report needs argument: inventory profit revenue')
