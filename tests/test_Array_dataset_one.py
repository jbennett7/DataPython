import unittest
from datapython.Array import Array

#@unittest.skip("Complete")
class TestArrayDataSetOne(unittest.TestCase):

    dataset = [ 5, 1, "bar", 2, "batz", 4, 3 , "foo" ]
    size = 10

    def setUp(self):
        self._ = Array(self.size)
        for _ in self.dataset:
            self._.insert(_)

    def test_getMaxNum(self):
        maxNum = self._.getMaxNum()
        _ = [i for i in self.dataset if isinstance(i, (int, float))]
        self.assertTrue(maxNum == max(_))

    def test_deleteMaxNum(self):
        arraySize = len(self._)
        maxNum = self._.deleteMaxNum()
        _ = [i for i in self.dataset if isinstance(i, (int, float))]
        self.assertTrue(maxNum == max(_))
        self.assertTrue(arraySize == len(self._)+1)
        self.assertTrue(self._.find(maxNum) == -1)

    # PP 2.3
    #@unittest.skip("Complete")
    def test_sortingScheme(self):
        newArray = Array(self.size)
        item = self._.deleteMaxNum()
        while item:
            newArray.insert(item)
            item = self._.deleteMaxNum()
        prev = newArray.get(0)
        for j in range(1,len(newArray)):
            prev = newArray.get(j)
            self.assertTrue(prev >= newArray.get(j))

        del(newArray)

    def tearDown(self):
        del(self._)
