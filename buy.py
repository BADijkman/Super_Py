# import sys
# import random
# from datetime import timedelta
# from console import console
# from getDateFromFile import getDateFromFile
# from utils import appendRowToBoughtCsv, appendRowToInventoryCsv


# sys.path.insert(0, "../csv")
# # sys.path.insert(0, "../utils") #AD


def handleBuy(parsed_Data):
    #     newId = random.randint(1000000, 9999999)
    name = parsed_Data.name.lower()
    print(name)
#     price = parsed_Data.price
#     amount = parsed_Data.amount
#     inputExpiration = parsed_Data.expiration  # ik wil datum ipv aant dagen

#     # ------
#     # Get the current day from file to set the expiration date
#     day = getDateFromFile("date")
#     euDay = day.strftime("%d-%m-%Y")
#     expiration = (day + timedelta(days=inputExpiration)).strftime("%d-%m-%Y")
#     # ------

#     try:
#         # Write new product to the inventory
#         # Append line to bought.csv
#         appendRowToBoughtCsv(newId, name, euDay, price, amount, expiration)

#         # Append line to inventory.csv
#         appendRowToInventoryCsv(newId, name, amount)

#         console.print("[blue bold]OK")
#     except:
#         print("An exception occurred")
