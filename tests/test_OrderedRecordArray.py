import unittest
from datapython.OrderedRecordArray import OrderedRecordArray

def second(x):
    return x[1]
    

#@unittest.skip("Already Tested")
class TestOrderedRecordArray(unittest.TestCase):

    data = [('a', 3.1), ('b', 7.5), ('c', 6.0), ('d', 3.1),
            ('e', 1.4), ('f', -1.2), ('g', 0.0), ('h', 7.5),
            ('i', 7.5), ('j', 6.0)]
    
    min_data = ('f', -1.2)
    find_found = 4 # ('a', 3.1)

    def setUp(self):
        self.size = len(self.data)
        self._ = OrderedRecordArray(self.size + 2, second)
        for _ in self.data:
            self._.insert(_)

    def test_length(self):
        self.assertTrue(len(self._) == self.size)

    def test_get_exception(self):
        with self.assertRaises(IndexError):
            self._.get(self.size)
        
    def test_get(self):
        self.assertTrue(self._.get(0) == self.min_data)

    def test_traverse(self):
        print()
        self._.traverse()

    def test_string(self):
        print(f"\n{str(self._)}\n")

    # More tests
    def test_find_found(self):
        self.assertTrue(self._.find(3.1) == 4)

    def test_find_not_found(self):
        self._.insert(('i', 8.0))
        self.assertTrue(self._.find(8.0) == 10)
        self.assertTrue(self._.find(7.6) == 10)

    def test_search_found(self):
        self.assertTrue(self._.search(1.4) == ('e',1.4))

    def test_search_not_found(self):
        self.assertIsNone(self._.search(7.6))

    def test_insert(self):
        self._.insert(('i', 8.0))
        self.assertTrue(self._.find(8.0) == 10)
        self._.insert(('j', 7.6))
        self.assertTrue(self._.find(7.6) == 10)

    def test_delete_true(self):
        self.assertTrue(self._.delete(('j', 6.0)))
        self.assertFalse(self._.delete(('i',8.0)))
