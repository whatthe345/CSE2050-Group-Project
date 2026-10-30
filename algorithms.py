def bubble_sort(products):
    """sort products by product ID using bubble sort."""
    for i in range(len(products) - 1):
        for j in range(len(products) - 1 - i):
            if products[j].get_id() > products[j + 1].get_id():
                products[j], products[j + 1] = products[j + 1], products[j]


def binary_search(products, product_id):
    """return the matching index in a sorted product list, or -1 ."""
    low = 0
    high = len(products) - 1

    while low <= high:
        middle = (low + high) // 2
        middle_id = products[middle].get_id()

        if middle_id == product_id:
            return middle
        elif middle_id < product_id:
            low = middle + 1
        else:
            high = middle - 1

    return -1

def selection_sort(products):
    """sort products in place by product ID using selection sort."""
    for i in range(len(products) - 1):
        max_index = 0

        for j in range(len(products) - i):
            if products[j].get_id() > products[max_index].get_id():
                max_index = j

        products[-1-i], products[max_index] = products[max_index], products[-1-i]