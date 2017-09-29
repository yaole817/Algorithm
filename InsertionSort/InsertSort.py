
class Solution(object):
    def insertionSort(self,A):
        """
        A type: list
        rtype : list
        """
        for j in range(1,len(A)):
            key = A[j]
            i = j-1
            while i >= 0 and A[i] > key:
                A[i+1] = A[i]
                i = i - 1
            A[i+1] = key
        return A

if __name__ == "__main__":
    array = [15,38,29,10,78,8,-7,100,6]
    s = Solution()
    print(s.insertionSort(array))
