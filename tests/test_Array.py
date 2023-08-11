import unittest
from src.Array import Array

@unittest.skip("Complete")
class TestArray(unittest.TestCase):

    def setUp(self):
        self.size = 4
        self._ = Array(self.size + 1)
        for _ in reversed(range(self.size)):
            self._.insert(_)

    def test_len(self):
        self.assertTrue(len(self._) == self.size)

    def test_get(self):
        self._.insert(1)
        _ = self._.get(self.size)
        self.assertTrue(_ == 1)

    def test_get_is_none(self):
        self.assertIsNone(self._.get(4))

    def test_set(self):
        self._.set(0,4)
        self.assertTrue(self._.get(0) == 4)

    def test_set_is_none(self):
        self.assertIsNone(self._.set(1,3))

    def test_insert(self):
        self._.insert(1)
        self.assertTrue(self._.get(self.size) == 1)

    def test_find_found(self):
        self.assertTrue(self._.find(3) == 0)

    def test_find_not_found(self):
        self.assertTrue(self._.find(5) == -1)

    def test_search_found(self):
        self.assertTrue(self._.search(3) == 3)
        
    def test_search_not_found(self):
        self.assertIsNone(self._.search(5))

    def test_delete_found(self):
        self.assertTrue(self._.delete(3))

    def test_delete_not_found(self):
        self.assertFalse(self._.delete(5))

    def test_traverse(self):
        print()
        self._.traverse()

    def tearDown(self):
        del(self._)

#if __name__ == '__main__':
#    unittest.main()
