import matplotlib.pyplot as plt
from handle_cvs import Inventory
from handle_date import Date


def checkForDuplicateProducts(list):
    updated_list = []
    for dict in list:
        for key, value in dict.items():
            if key == "name":
                search_value = value
            elif key == "amount":
                input_Amount = value

        # If the search_value is found modify amount
        new_dict = True
        for dict in updated_list:
            if search_value in dict.values():
                amount = dict.get("amount")
                new_Amount = amount + input_Amount
                dict["amount"] = new_Amount
                new_dict = False
                break
        # If the search_value is not found, create a new dictionary
        if new_dict:
            new_dict = {"name": search_value, "amount": input_Amount}
            updated_list.append(new_dict)

    return (updated_list)


def pltShow():
    # get Inventory
    inStockTotalNotExpired = Inventory.totalNotExpired()

    # check duplicate items and if so modify amount
    listWithoutDuplicateProducts = checkForDuplicateProducts(
        inStockTotalNotExpired)

    products = [d['name'] for d in listWithoutDuplicateProducts]
    amounts = [d['amount'] for d in listWithoutDuplicateProducts]

    fig, ax = plt.subplots()

    date = Date.getDateFromFile("str")
    ax.set_title(f'Inventory {date}')
    ax.set_ylabel('amount')
    bar_colors = ['tab:blue', 'tab:cyan']

    ax.bar(products, amounts,  color=bar_colors)

    plt.show()
