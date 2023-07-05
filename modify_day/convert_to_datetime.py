from datetime import datetime


def convert_to_datetime(date_string):
    return datetime.strptime(date_string, "%d/%m/%Y")
