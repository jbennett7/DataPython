import unittest
from src.OrderedArray import OrderedArray

class TestOrderedArray(unittest.TestCase):

    def setUp(self):
        self.size = 4
        self._ = OrderedArray(self.size + 2)
        for _ in reversed(range(self.size)):
            self._.insert(_)

    def test_len(self):
        self.assertTrue(len(self._) == self.size)

    def test_get(self):
        self.assertTrue(self._.get(0) == 0)

    def test_get_exception(self):
        with self.assertRaises(IndexError):
            self._.get(self.size)

    def test_traverse(self):
        print()
        self._.traverse()

    def test_string(self):
        print(f"\n{str(self._)}\n")

    def test_find_found(self):
        self.assertTrue(self._.find(1) == 1)

    def test_find_not_found(self):
        self._.insert(5)
        self.assertTrue(self._.find(5) == 4)
        self.assertTrue(self._.find(4) == 4)

    def test_search_found(self):
        self.assertTrue(self._.search(3) == 3)

    def test_search_not_found(self):
        self.assertIsNone(self._.search(4))

    def test_insert(self):
        self._.insert(5)
        self.assertTrue(self._.find(5) == 4)
        self._.insert(4)
        self.assertTrue(self._.find(4) == 4)

    def test_delete_true(self):
        self.assertTrue(self._.get(2) == 2)
        self.assertTrue(self._.delete(2))
        self.assertTrue(self._.get(2) == 3)

    def test_delete_false(self):
        self.assertFalse(self._.delete(4))
