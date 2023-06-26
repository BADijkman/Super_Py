import os
import csv
from date import get_date
from console import console


def init_data(base_path, csv_path):
    # check cvs path
    if os.path.exists(csv_path):
        pass
    else:
        os.mkdir(f'{base_path}/csv')

    # check bought.cvs excist

    if os.path.exists(f'{csv_path }/bought.csv'):
        pass
    else:
        fieldnames = ['id', 'product_name', 'amount', 'buy_price',
                      'buy_date',  'expiration_date']
        with open(f'{csv_path }/bought.csv', 'w', encoding='UTF8', newline='') as f:
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
                      'amount']
        with open(f'{csv_path }/inventory.csv', 'w', encoding='UTF8', newline='')as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # set date

    with open("./day/day.txt", "w") as f:
        euDay = get_date()
        console.print(f"[green]Current day set to: {euDay}")
        f.write(euDay)
