import os
import csv
from handle_date import Date


def init_data(base_path, csv_path, current_date_path):
    # check cvs path
    if os.path.exists(csv_path):
        pass
    else:
        os.mkdir(f'{base_path}/csv')

    # check purchase.cvs excist
    if os.path.exists(f'{csv_path }/purchase.csv'):
        pass
    else:
        fieldnames = ['id', 'product_name', 'amount', 'buy_price',
                      'buy_date',  'expiration_date']
        with open(f'{csv_path }/purchase.csv', 'w',
                  encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check sold.csv excist
    if os.path.exists(f'{csv_path}/sold.csv'):
        pass
    else:
        fieldnames = ['id', 'product_name', 'amount',
                      'sell_date', 'sell_price']

        with open(f'{csv_path }/sold.csv', 'w',
                  encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check inventory.csv excist
    if os.path.exists(f'{csv_path }/inventory.csv'):
        pass
    else:
        fieldnames = ['id', 'name',
                      'amount', 'buy_date', 'expiration_date']
        with open(f'{csv_path }/inventory.csv', 'w',
                  encoding='UTF8', newline='')as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check day path
    if os.path.exists(current_date_path):
        pass
    else:
        os.mkdir(f'{base_path}/current_date')
        # set day to today
        with open("./current_date/day.txt", "w") as f:
            newdate = Date.get_date()
            f.write(newdate)
