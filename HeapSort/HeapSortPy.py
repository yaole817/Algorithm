class HeapSrot():
    def __init__(self, array):
        self.array = array
    
    def sort(self):
        N = len(self.array) - 1
        base = 0
        for k in range(N // 2, base - 1, -1):
            self.__sink(self.array, k, N)
        while N > base:
            self.exch(self.array, base, N)
            N -= 1
            self.__sink(self.array, base, N)

    def __sink(self, array, k, N):
        while 2 * k <= N:
            j = 2 * k
            if j < N  and (array[j] < array[j + 1]):
                j += 1
            if array[k] >= array[j]: break
            self.exch(array, k, j)
            k = j

    def exch(self, array, i, j):
        array[j], array[i] = array[i], array[j]

if __name__ == "__main__":
    a = [6, -2, 7, 3, 4, 10, 9, 8, 28, -5, 1, -9]
    heapSrot = HeapSrot(a)
    heapSrot.sort()
    print(a)