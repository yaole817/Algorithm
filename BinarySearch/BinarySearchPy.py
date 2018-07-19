class BinarySearch:
    def __init__(self, array):
        self.__array = array
    
    def search(self, num):
        length = len(self.__array) - 1
        result = self.__search(self.__array, num, 0, length)
        if self.__array[result] == num:
            return result
        else:
            return -1
    
    def __search(self, array, num, lo, hi):
        if hi < lo: return lo
        mid = (hi - lo) // 2 + lo
        if array[mid] == num:
            return mid
        elif array[mid] < num:
            return self.__search(array, num, mid + 1, hi)
        else:
            return self.__search(array, num, lo, mid - 1)

class BinarySearch1:
    def __init__(self, array):
        self.__array = array
    
    def search(self, num):
        length = len(self.__array) - 1
        result = self.__search(self.__array, num, 0, length)
        if self.__array[result] == num:
            return result
        else:
            return -1
    
    def __search(self, array, num, lo, hi):
        while lo < hi:
            print(array[lo:hi+1])
            mid = (hi - lo) // 2 + lo
            if array[mid] == num:
                return mid
            elif array[mid] < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

if __name__ == "__main__":
    a = [-9, -5, -2, 1, 3, 4, 6, 7, 8, 9, 10, 28]
    binarySearch = BinarySearch(a)
    index = binarySearch.search(6)
    print(index)

    binarySearch = BinarySearch1(a)
    index = binarySearch.search(-5)
    print(index)