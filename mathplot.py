import matplotlib.pyplot as plt
from utils.utils import inStocktotal, inStockTotalNotExpired


def pltShow():
    # get Inventory
    instock = inStocktotal()
    inStockTotal = inStockTotalNotExpired(instock)
    print(inStockTotal)

    fig, ax = plt.subplots()

    # newList = []
    newDict = {}
    for dict in inStockTotal:
        
        
   

    # newDict=
    # newList.append(newDict)

    # print(inStockSorted)
    fruits = ["apple", "pear"]
    counts = [5, 5]
    bar_colors = ['tab:green', 'tab:blue']

    ax.bar(fruits, counts,  color=bar_colors)

    ax.set_title('Inventory')
    ax.set_ylabel('amount')

    plt.show()
