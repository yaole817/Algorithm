class Solution(object):
    def heapSort(self, A):
        n = len(A)
        first = int(n/2 - 1)
        for start in range(first, -1 ,-1):
            self.maxHeapify(A,start, n-1)
        for end in range(n-1, 0, -1):
            A[end], A[0] = A[0], A[end]
            self.maxHeapify(A, 0, end-1)

    def maxHeapify(self, A, start, end):
        root = start
        while True:
            child = root * 2 + 1 # get the child
            if child > end : break
            if child + 1 <= end and A[child] < A[child+1]:
                child = child + 1
            if A[root] < A[child]:
                A[root], A[child] = A[child], A[root] # exchange
                root = child
            else: break


if __name__ == "__main__":
    array = [15,38,29,10,78,8,-7,100,76,-19]
    s = Solution()
    s.heapSort(array)
    print(array)