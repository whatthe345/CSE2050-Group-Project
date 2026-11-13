
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




def merge_sort(products):
    """Sort products in place by product ID using merge sort."""
    if len(products) <= 1:
        return

    middle = len(products) // 2
    A = products[:middle]
    B = products[middle:]

    merge_sort(A)
    merge_sort(B)

    i = 0 
    j = 0 
    while i < len(A) and j < len(B):
        if A[i].get_id() < B[j].get_id():
            products[i + j] = A[i]
            i = i + 1
        else:
            products[i + j] = B[j]
            j = j + 1

    
    products[i + j:] = A[i:] + B[j:]

def partition(products, i, j):
    """Partition products and return the pivot's final index."""
    pivot = j - 1
    j = pivot - 1

    while i < j:
        while products[i].get_id() < products[pivot].get_id():
            i = i + 1

        while i < j and products[j].get_id() >= products[pivot].get_id():
            j = j - 1

        if i < j:
            products[i], products[j] = products[j], products[i]

    if products[i].get_id() >= products[pivot].get_id():
        products[pivot], products[i] = products[i], products[pivot]
        pivot = i

    return pivot


def quick_sort_helper(products, left, right):
    """Sort products from left up to, but excluding, right."""
    if right - left <= 1:
        return

    pivot = partition(products, left, right)

    quick_sort_helper(products, left, pivot)
    quick_sort_helper(products, pivot + 1, right)


def quick_sort(products):
    """Sort products in place by product ID using quick sort."""
    quick_sort_helper(products, 0, len(products))

def quick_select_helper(products, k, left, right):
    """Find the kth smallest product by searching one partition."""
    if right - left == 1:
        return products[left]

    pivot = partition(products, left, right)

    if k <= pivot:
        return quick_select_helper(products, k, left, pivot)
    elif k == pivot + 1:
        return products[pivot]
    else:
        return quick_select_helper(products, k, pivot + 1, right)


def quick_select(products, k):
    """Return the kth smallest product by ID, or None for an invalid rank."""
    if k < 1 or k > len(products):
        return None

    return quick_select_helper(products, k, 0, len(products))

