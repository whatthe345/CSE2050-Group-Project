import unittest
from product import Product
from store import Store
from algorithms import bubble_sort, selection_sort, binary_search


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


if __name__ == "__main__":
    unittest.main()