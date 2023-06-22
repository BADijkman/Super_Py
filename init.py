import os
import csv


def init_data(base_path, cvs_path):
    # check cvs path
    if os.path.exists(cvs_path):
        pass
    else:
        os.mkdir(f'{base_path}/cvs')

    # check bought.cvs excist
    if os.path.exists(f'{cvs_path }/bought.csv'):
        pass
    else:
        fieldnames = ['id', 'product_name', 'amount', 'buy_price',
                      'buy_date',  'expiration_date']
        with open(f'{cvs_path }/bought.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check sold.cvs excist
    if os.path.exists(f'{cvs_path }/sold.csv'):
        pass
    else:
        fieldnames = ['id', 'name', 'amount',
                      'sell_date', 'sell_price']

        with open(f'{cvs_path }/sold.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()

    # check inventory.cvs excist
    if os.path.exists(f'{cvs_path }/inventory.csv'):
        pass
    else:
        fieldnames = ['id', 'name',
                      'amount']
        with open(f'{cvs_path }/inventory.csv', 'w', encoding='UTF8', newline='')as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()
