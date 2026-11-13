import unittest
from store import Store
from product import Product
from algorithms import merge_sort, quick_sort, quick_select
from hashMapping import HashMapping


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
        class TestHashMapping(unittest.TestCase):
    """Test HashMapping through its public behavior only."""

    def test_put_and_get(self):
        table = HashMapping()
        table.put("BMW-M3", "Blue BMW M3")
        table.put("AUDI-R8", "Red Audi R8")

        self.assertEqual(table.get("BMW-M3"), "Blue BMW M3")
        self.assertEqual(table.get("AUDI-R8"), "Red Audi R8")
        self.assertIn("BMW-M3", table)
        self.assertNotIn("MERC-C63", table)
        self.assertEqual(len(table), 2)

    def test_missing_key_raises_key_error(self):
        table = HashMapping()
        with self.assertRaises(KeyError):
            table.get("MERC-C63")

        table.put("BMW-M3", "BMW M3")
        with self.assertRaises(KeyError):
            table.get("MERC-C63")

    def test_update_existing_key(self):
        table = HashMapping()
        table.put("BMW-M3", "Blue BMW M3")
        table.put("BMW-M3", "Black BMW M3")

        self.assertEqual(table.get("BMW-M3"), "Black BMW M3")
        self.assertEqual(len(table), 1)

    def test_collisions_keep_every_entry(self):
        # Many keys in a tiny default table forces keys to share buckets
        table = HashMapping()
        keys = [0, 2, 4, 6, 8, 10]
        for key in keys:
            table.put(key, f"value-{key}")

        for key in keys:
            self.assertEqual(table.get(key), f"value-{key}")
        self.assertEqual(len(table), len(keys))

        # Updating a key that is not first in its bucket must also work
        table.put(10, "updated")
        self.assertEqual(table.get(10), "updated")
        self.assertEqual(table.get(0), "value-0")
        self.assertEqual(len(table), len(keys))

    def test_rehash_preserves_entries(self):
        table = HashMapping()
        keys = [f"CAR-{i}" for i in range(8)]
        for key in keys:
            table.put(key, key.lower())

        table.rehash()
        table.rehash()

        for key in keys:
            self.assertEqual(table.get(key), key.lower())
            self.assertIn(key, table)
        self.assertEqual(len(table), len(keys))

        # Table still works normally after rehashing
        table.put("CAR-NEW", "new")
        table.put("CAR-0", "changed")
        self.assertEqual(table.get("CAR-NEW"), "new")
        self.assertEqual(table.get("CAR-0"), "changed")
        self.assertEqual(len(table), len(keys) + 1)


class TestStoreIntegration(unittest.TestCase):
    """Test Store methods that use sorting, QuickSelect, and the hash mapping."""

    def setUp(self):
        self.store = Store()
        self.m5 = Product("BMW-M5", "BMW M5", 110000)
        self.rs7 = Product("AUDI-RS7", "Audi RS7", 125000)
        self.e63 = Product("MERC-E63", "Mercedes E63", 115000)
        for product in (self.m5, self.rs7, self.e63):
            self.assertTrue(self.store.add_product(product))

    def test_sorting_methods_order_products_by_id(self):
        expected = ["AUDI-RS7", "BMW-M5", "MERC-E63"]

        self.store.merge_sort_products()
        self.assertEqual([p.get_id() for p in self.store.products], expected)

        # Reverse the order, then sort with quick sort
        self.store.products.reverse()
        self.store.quick_sort_products()
        self.assertEqual([p.get_id() for p in self.store.products], expected)

        # Binary search works on the sorted catalog
        self.assertIs(self.store.binary_search_product("BMW-M5"), self.m5)
        self.assertIsNone(self.store.binary_search_product("FORD-GT"))

    def test_quick_select_product(self):
        self.assertIs(self.store.quick_select_product(1), self.rs7)
        self.assertIs(self.store.quick_select_product(2), self.m5)
        self.assertIs(self.store.quick_select_product(3), self.e63)

        self.assertIsNone(self.store.quick_select_product(0))
        self.assertIsNone(self.store.quick_select_product(4))
        self.assertIsNone(Store().quick_select_product(1))

    def test_hash_based_find_product(self):
        self.assertIs(self.store.find_product("BMW-M5"), self.m5)
        self.assertIs(self.store.find_product("AUDI-RS7"), self.rs7)
        self.assertIsNone(self.store.find_product("FORD-GT"))

        # A duplicate ID is rejected and the original product is kept
        duplicate = Product("BMW-M5", "Fake BMW M5", 1)
        self.assertFalse(self.store.add_product(duplicate))
        self.assertIs(self.store.find_product("BMW-M5"), self.m5)

    def test_find_product_after_sorting_and_many_products(self):
        extra = [Product(f"CAR-{i:03d}", f"Car {i}", 1000 + i) for i in range(20)]
        for product in extra:
            self.store.add_product(product)

        self.store.merge_sort_products()

        for product in extra:
            self.assertIs(self.store.find_product(product.get_id()), product)
        self.assertIs(self.store.find_product("BMW-M5"), self.m5)



if __name__ == "__main__":
    unittest.main()