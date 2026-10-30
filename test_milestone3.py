import unittest
from product import Product
from store import Store
from algorithms import bubble_sort, selection_sort, binary_search, insertion_sort, recursive_total_price,fewest_coins


class TestMyAlgorithms(unittest.TestCase):
    """Test bubble sort, selection sort, and binary search."""

    def test_bubble_sort(self):
        p1 = Product("P100", "Notebook", 4.99)
        p2 = Product("P200", "Backpack", 34.99)
        p3 = Product("P300", "Pencil", 1.99)
        products = [p3, p1, p2]

        bubble_sort(products)

        self.assertEqual(products, [p1, p2, p3])

    def test_selection_sort_reverse_order(self):
        p1 = Product("P100", "Notebook", 4.99)
        p2 = Product("P200", "Backpack", 34.99)
        p3 = Product("P300", "Pencil", 1.99)
        products = [p3, p2, p1]

        selection_sort(products)

        self.assertEqual(products, [p1, p2, p3])
    def test_insertion_sort(self):
        p1 = Product("P100", "Notebook", 4.99)
        p2 = Product("P200", "Backpack", 34.99)
        p3 = Product("P300", "Pencil", 1.99)
        products = [p2, p3, p1]
 
        insertion_sort(products)
 
        self.assertEqual(products, [p1, p2, p3])
 
    def test_sorting_edge_cases(self):
        p1 = Product("P100", "Notebook", 4.99)
        p2 = Product("P200", "Backpack", 34.99)

        for sorting_alg in [bubble_sort, selection_sort]:
            products = []
            sorting_alg(products)
            self.assertEqual(products, [])

            products = [p1]
            sorting_alg(products)
            self.assertEqual(products, [p1])

            products = [p1, p2]
            sorting_alg(products)
            self.assertEqual(products, [p1, p2])

    def test_binary_search_first_item(self):
        p1 = Product("P100", "Notebook", 4.99)
        p2 = Product("P200", "Backpack", 34.99)
        p3 = Product("P300", "Pencil", 1.99)
        products = [p1, p2, p3]

        self.assertEqual(binary_search(products, "P100"), 0)

    def test_binary_search_middle_item(self):
        p1 = Product("P100", "Notebook", 4.99)
        p2 = Product("P200", "Backpack", 34.99)
        p3 = Product("P300", "Pencil", 1.99)
        products = [p1, p2, p3]

        self.assertEqual(binary_search(products, "P200"), 1)

    def test_binary_search_not_found(self):
        p1 = Product("P100", "Notebook", 4.99)
        products = [p1]

        self.assertEqual(binary_search(products, "P999"), -1)
        self.assertEqual(binary_search([], "P999"), -1)

    def test_store_binary_lookup(self):
        store = Store()
        p1 = Product("P100", "Notebook", 4.99)
        p2 = Product("P200", "Backpack", 34.99)

        store.add_product(p2)
        store.add_product(p1)
        store.bubble_sort_products()

        self.assertEqual(store.binary_search_product("P100"), p1)
        self.assertIsNone(store.binary_search_product("P999"))
    def test_recursive_total_price_empty_list(self):
        self.assertEqual(recursive_total_price([]), 0)
 
    def test_recursive_total_price_multiple_products(self):
        p1 = Product("P100", "Notebook", 4.99)
        p2 = Product("P200", "Backpack", 34.99)
        p3 = Product("P300", "Pencil", 1.99)
        products = [p1, p2, p3]
 
        self.assertAlmostEqual(recursive_total_price(products), 41.97)
 
    def test_fewest_coins_amount_zero(self):
        self.assertEqual(fewest_coins([1, 5, 10, 25], 0), 0)
 
    def test_fewest_coins_exact_coin(self):
        self.assertEqual(fewest_coins([1, 5, 10, 25], 25), 1)
 
    def test_fewest_coins_larger_amount(self):
        # 25 + 25 + 10 + 1 + 1 + 1
        self.assertEqual(fewest_coins([1, 5, 10, 25], 63), 6)
 
    def test_fewest_coins_not_greedy(self):
        # Greedy would pick 4 + 1 + 1 (3 coins); the best is 3 + 3 (2 coins)
        self.assertEqual(fewest_coins([1, 3, 4], 6), 2)
 
    def test_fewest_coins_impossible_amount(self):
        self.assertEqual(fewest_coins([2], 3), -1)
    def test_store_sort_integration(self):
        p1 = Product("P100", "Notebook", 4.99)
        p2 = Product("P200", "Backpack", 34.99)
        p3 = Product("P300", "Pencil", 1.99)
 
        for sort_method in ["bubble_sort_products",
                            "selection_sort_products",
                            "insertion_sort_products"]:
            store = Store()
            store.add_product(p3)
            store.add_product(p1)
            store.add_product(p2)
 
            getattr(store, sort_method)()
 
            self.assertEqual(store.products, [p1, p2, p3])
 
    def test_store_recursive_catalog_total(self):
        store = Store()
        store.add_product(Product("P100", "Notebook", 4.99))
        store.add_product(Product("P200", "Backpack", 34.99))
 
        self.assertAlmostEqual(store.recursive_catalog_total(), 39.98)
        # Calculating the total should not remove products from the store
        self.assertEqual(len(store.products), 2)
 
    def test_store_calculate_change(self):
        store = Store()
 
        self.assertEqual(store.calculate_change([1, 5, 10, 25], 63), 6)
        self.assertEqual(store.calculate_change([1, 5, 10, 25], 0), 0)
        self.assertEqual(store.calculate_change([2], 3), -1)

if __name__ == "__main__":
    unittest.main()