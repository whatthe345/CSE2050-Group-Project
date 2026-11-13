import unittest
from store import Store
from product import Product
from algorithms import merge_sort, quick_sort, quick_select


class TestMergeSort(unittest.TestCase):
    """Test merge sort using car product IDs."""

    def test_empty_and_one_product(self):
        products = []
        self.assertIsNone(merge_sort(products))
        self.assertEqual(products, [])

        product = Product("BMW-M3", "BMW M3", 76000)
        products = [product]

        self.assertIsNone(merge_sort(products))
        self.assertEqual(products, [product])

    def test_reverse_order(self):
        products = [
            Product("CAR-C", "BMW M4", 80000),
            Product("CAR-B", "Mercedes C63", 85000),
            Product("CAR-A", "Audi RS5", 79000)
        ]

        self.assertIsNone(merge_sort(products))

        self.assertEqual(
            [product.get_id() for product in products],
            ["CAR-A", "CAR-B", "CAR-C"]
        )

    def test_duplicates_and_already_sorted(self):
        first = Product("BMW-M3", "Blue BMW M3", 76000)
        second = Product("BMW-M3", "Black BMW M3", 78000)
        third = Product("MERC-C63", "Mercedes C63", 85000)
        products = [third, first, second]

        merge_sort(products)

        self.assertEqual(
            [product.get_id() for product in products],
            ["BMW-M3", "BMW-M3", "MERC-C63"]
        )
        self.assertCountEqual(products, [first, second, third])

        merge_sort(products)

        self.assertEqual(
            [product.get_id() for product in products],
            ["BMW-M3", "BMW-M3", "MERC-C63"]
        )


class TestQuickSort(unittest.TestCase):
    """Test quick sort using car product IDs."""

    def test_empty_and_one_product(self):
        products = []
        self.assertIsNone(quick_sort(products))
        self.assertEqual(products, [])

        product = Product("AUDI-R8", "Audi R8", 160000)
        products = [product]

        self.assertIsNone(quick_sort(products))
        self.assertEqual(products, [product])

    def test_reverse_order(self):
        products = [
            Product("MERC-E63", "Mercedes E63", 115000),
            Product("BMW-M5", "BMW M5", 110000),
            Product("AUDI-RS7", "Audi RS7", 125000)
        ]

        self.assertIsNone(quick_sort(products))

        self.assertEqual(
            [product.get_id() for product in products],
            ["AUDI-RS7", "BMW-M5", "MERC-E63"]
        )

    def test_duplicates_and_already_sorted(self):
        first = Product("AUDI-R8", "Red Audi R8", 160000)
        second = Product("AUDI-R8", "White Audi R8", 165000)
        third = Product("BMW-M4", "BMW M4", 80000)
        products = [third, first, second]

        quick_sort(products)

        self.assertEqual(
            [product.get_id() for product in products],
            ["AUDI-R8", "AUDI-R8", "BMW-M4"]
        )
        self.assertCountEqual(products, [first, second, third])

        quick_sort(products)

        self.assertEqual(
            [product.get_id() for product in products],
            ["AUDI-R8", "AUDI-R8", "BMW-M4"]
        )


class TestQuickSelect(unittest.TestCase):
    """Test valid and invalid QuickSelect ranks using cars."""

    def test_first_and_last_rank(self):
        largest = Product("MERC-C63", "Mercedes C63", 85000)
        smallest = Product("AUDI-RS5", "Audi RS5", 79000)
        middle = Product("BMW-M3", "BMW M3", 76000)
        products = [largest, smallest, middle]

        self.assertIs(quick_select(products, 1), smallest)
        self.assertIs(quick_select(products, 3), largest)
        self.assertCountEqual(products, [largest, smallest, middle])

    def test_middle_rank_and_duplicates(self):
        products = [
            Product("MERC-E63", "Mercedes E63", 115000),
            Product("AUDI-RS7", "Audi RS7", 125000),
            Product("BMW-M5", "BMW M5", 110000)
        ]

        self.assertEqual(
            quick_select(products, 2).get_id(),
            "BMW-M5"
        )

        products = [
            Product("BMW-M4", "BMW M4", 80000),
            Product("AUDI-R8", "Red Audi R8", 160000),
            Product("AUDI-R8", "White Audi R8", 165000)
        ]

        self.assertEqual(
            quick_select(products, 2).get_id(),
            "AUDI-R8"
        )

        product = Product("BMW-M3", "BMW M3", 76000)
        self.assertIs(quick_select([product], 1), product)

    def test_invalid_ranks(self):
        products = [Product("MERC-C63", "Mercedes C63", 85000)]

        self.assertIsNone(quick_select(products, 0))
        self.assertIsNone(quick_select(products, -1))
        self.assertIsNone(quick_select(products, 2))
        self.assertIsNone(quick_select([], 1))


if __name__ == "__main__":
    unittest.main()