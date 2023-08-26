import unittest
from datapython.Array import Array

#@unittest.skip("Complete")
class TestArrayDataSetTwo(unittest.TestCase):

    dataset = [ "joe", "jen", "wanda", "james" ]
    size = 10

    def setUp(self):
        self._ = Array(self.size)
        for _ in self.dataset:
            self._.insert(_)

    def test_getMaxNum(self):
        maxNum = self._.getMaxNum()
        _ = [i for i in self.dataset if isinstance(i, (int, float))]
        self.assertIsNone(maxNum)

    def test_deleteMaxNum(self):
        arraySize = len(self._)
        maxNum = self._.deleteMaxNum()
        _ = [i for i in self.dataset if isinstance(i, (int, float))]
        self.assertIsNone(maxNum)
        self.assertTrue(arraySize == len(self._))

    # PP 2.3
    #@unittest.skip("Complete")
    def test_sortingScheme(self):
        newArray = Array(self.size)
        item = self._.deleteMaxNum()
        self.assertIsNone(item)

        del(newArray)

    def tearDown(self):
        del(self._)


