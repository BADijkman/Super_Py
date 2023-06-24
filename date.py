from datetime import datetime


def get_date():
    return datetime.today().strftime('%d/%m/%Y')
