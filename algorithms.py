
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
memo = {}
def recursive_total_price(products):
    """Return the total of all product prices using recursion."""
    if len(products) == 0:
        return 0
    return products[0].get_price() + recursive_total_price(products[1:])
def fewest_coins(coins, amount):
    """Return the minimum number of coins needed to make `amount`
    using top-down memoization. Returns -1 if it can't be made."""
    memo = {}

    def helper(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float("inf")
        if remaining in memo:
            return memo[remaining]

        best = float("inf")
        for coin in coins:
            best = min(best, helper(remaining - coin) + 1)

        memo[remaining] = best
        return best

    result = helper(amount)
    return result if result != float("inf") else -1

def insertion_sort(products) :
    """insertion sortsort"""
    n = len(products)
    for i in range(1, n):
        key = products[i]
        keyid = key.get_id()
        j = i - 1
        while j >= 0 and products[j].get_id() > keyid:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key
    return products


