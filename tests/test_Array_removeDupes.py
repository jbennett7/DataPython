import unittest
from datapython.Array import Array

#@unittest.skip("Complete")
class TestArrayRemoveDupes(unittest.TestCase):

    dataset = [ 5, 1, "bar", 2, "batz", 4, 3 , "foo", "bar", 2, "batz", "bar", "batz", 4, 3 , "foo" ]
    size = len(dataset)

    def setUp(self):
        self._ = Array(self.size)
        for _ in self.dataset:
            self._.insert(_)

    def test_remove_dupes(self):
        self._.removeDupes()
        print()
        print("Remove Dupes")
        self._.traverse()
        print()
