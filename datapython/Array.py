class Array(object):

    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]

    def set(self, n, value):
        if 0 <= n and n < self.__nItems:
            self.__a[n] = value

    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1

    def search(self, item):
        return self.get(self.find(item))

    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True
        return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    # page 73, PP 2.1
    def getMaxNum(self):
        maxNum = None
        for _ in self.__a:
            if isinstance(_, (int, float)):
                if maxNum == None or _ > maxNum:
                    maxNum = _
        return maxNum

    # PP 2.2
    def deleteMaxNum(self):
        maxNum = self.getMaxNum()
        self.delete(maxNum)
        return maxNum 

    # PP 2.3
    def removeDupes(self):
        _ = [None] * self.__nItems
        _nItems = 0
        for j in range(self.__nItems):
            found = False
            for k in range(_nItems):
                if self.__a[j] == _[k]:
                    found = True
                    break
            if not found:
                _[_nItems] = self.__a[j]
                _nItems+=1
        self.__a = _
        self.__nItems = _nItems
