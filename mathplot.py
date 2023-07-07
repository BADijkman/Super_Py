import matplotlib.pyplot as plt
from utils.utils import inStocktotal, inStockTotalNotExpired


def checkForDuplicateProducts(new_list):
    updated_list = []
    for dict in new_list:
        for key, value in dict.items():
            if key == "name":
                search_value = value
            elif key == "amount":
                input_Amount = value

        new_dict = True
    # Check if the search_value exists in any of the dictionaries and       modify amount
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
    instock = inStocktotal()
    inStockTotal = inStockTotalNotExpired(instock)
    # print(inStockTotal)
    listWithoutDuplicateProducts = checkForDuplicateProducts(inStockTotal
                                                             )

    # products = [d['name'] for d in listWithoutDuplicateProducts]
    # amounts = [d['amount'] for d in listWithoutDuplicateProducts]

    fig, ax = plt.subplots()

    products = [d['name'] for d in listWithoutDuplicateProducts]
    amounts = [d['amount'] for d in listWithoutDuplicateProducts]
    bar_colors = ['tab:green', 'tab:blue']

    ax.bar(products, amounts,  color=bar_colors)

    ax.set_title('Inventory')
    ax.set_ylabel('amount')

    plt.show()
