import unittest
from datapython.Array import Array

#@unittest.skip("Complete")
class TestArrayBasic(unittest.TestCase):

    dataset = [ 5, 1, "bar", 2, "batz", 4, 3 , "foo" ]
    size = 10

    def setUp(self):
        self._ = Array(self.size)
        for _ in self.dataset:
            self._.insert(_)

    def test_len(self):
        self.assertTrue(len(self._) == len(self.dataset))

    def test_get(self):
        self._.insert(1)
        _ = self._.get(len(self.dataset))
        self.assertTrue(_ == 1)

    def test_get_is_none(self):
        self.assertIsNone(self._.get(8))

    def test_set(self):
        self._.set(0,4)
        self.assertTrue(self._.get(0) == 4)

    def test_set_is_none(self):
        self.assertIsNone(self._.set(1,3))

    def test_insert(self):
        self._.insert(1)
        self.assertTrue(self._.get(len(self.dataset)) == 1)

    def test_find_found(self):
        idx = self._.find(3)
        self.assertTrue(self._.get(idx) == 3)

    def test_find_not_found(self):
        self.assertTrue(self._.find(8) == -1)

    def test_search_found(self):
        self.assertTrue(self._.search(3) == 3)
        
    def test_search_not_found(self):
        self.assertIsNone(self._.search(8))

    def test_delete_found(self):
        self.assertTrue(self._.delete(3))

    def test_delete_not_found(self):
        self.assertFalse(self._.delete(8))

    def test_traverse(self):
        print()
        self._.traverse()
