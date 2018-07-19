class QuickSort():
    def sort(self, array):
        self.__sort(array, 0, len(array) - 1)

    def __sort(self, array, lo, hi):
        if hi <= lo: return
        index = self.__partion(array, lo, hi)
        self.__sort(array, lo, index)
        self.__sort(array, index + 1, hi)
        
    def __partion(self, array, lo, hi):
        pickNumber = array[lo]
        i, j = lo, hi
        while i < j:
            while array[j] >= pickNumber and j > i: j -= 1
            self.exch(array, i, j)
            while array[i] <= pickNumber and i < j: i += 1
            self.exch(array, i, j)
        return j
    def exch(self, array, i, j):
        array[j], array[i] = array[i], array[j]
        return array

if __name__ == "__main__":
    a = [6, -2, 7, 3, 4, 10, 9, 8, 28, -5, 1, -9]
    quickSort = QuickSort()
    quickSort.sort(a)
    print(a)
        



