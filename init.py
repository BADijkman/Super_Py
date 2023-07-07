import os
import csv
from modify_day.date import get_date


def init_data(base_path, csv_path, day_path):
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
        with open(f'{csv_path }/purchase.csv','w',encoding='UTF8', newline='')'as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check sold.csv excist
    if os.path.exists(f'{csv_path}/sold.csv'):
        pass
    else:
        fieldnames = ['id', 'product_name', 'amount',
                      'sell_date', 'sell_price']

        with open(f'{csv_path }/sold.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check inventory.csv excist
    if os.path.exists(f'{csv_path }/inventory.csv'):
        pass
    else:
        fieldnames = ['id', 'name',
                      'amount', 'expiration_date']
        with open(f'{csv_path }/inventory.csv', 'w', encoding='UTF8', newline='')as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check day path
    if os.path.exists(day_path):
        pass
    else:
        os.mkdir(f'{base_path}/day')
        # set day to today
        with open("./day/day.txt", "w") as f:
            euDay = get_date()
            f.write(euDay)
