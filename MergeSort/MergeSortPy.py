class Merge:
    def __init__(self):
        self.cacheArray = []
        self.array = []

    def sort(self, array):
        self.cacheArray = [i for i in array]
        self.array = array
        self.__sort(0, len(self.array) - 1)

    def __sort(self, lo, hi):
        if hi <= lo: return
        mid = (hi - lo) // 2 + lo
        self.__sort(lo, mid)
        self.__sort(mid + 1, hi)
        self.__merge(lo, mid, hi)
    
    def __merge(self, lo, mid, hi):
        i, j = lo, mid + 1
        self.cacheArray[lo : hi + 1] = self.array[lo : hi + 1]
        for k in range(lo, hi + 1):
            if i > mid: 
                self.array[k] = self.cacheArray[j]
                j += 1
            elif j > hi:
                self.array[k] = self.cacheArray[i]
                i += 1
            elif self.cacheArray[i] > self.cacheArray[j]:
                self.array[k] = self.cacheArray[j]
                j += 1
            else:
                self.array[k] = self.cacheArray[i]
                i += 1
                

if __name__ == "__main__":
    numbers = [3, 1, 6, 9, 10, 0, -1, 45, 2, 44, 83, -28]
    merge = Merge()
    merge.sort(numbers)
    print(numbers)
    
