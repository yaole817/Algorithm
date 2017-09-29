
class Solution(object):
    def partition(self, A, low, high):
        pivot = A[low]  # as the base
        while low < high:
            while low < high and A[high] >= pivot: high -= 1
            A[low] = A[high] 
            while low < high and A[low] < pivot: low += 1
            A[high] = A[low]           
        A[low] = pivot
        print(A)
        return low
    
    def quickSort(self, A, low, high):
        if low < high:
            pivotIndex = self.partition(A, low, high)
            self.quickSort(A, low, pivotIndex-1)
            self.quickSort(A, pivotIndex+1, high)
        return A

class Solution1(object):
    def partition(self, Arr, left, right):
        pivot = Arr[right]
        i = left - 1
        for j in range(left, right):
            if Arr[j] <= pivot:
                i = i+1
                Arr[i],Arr[j] = Arr[j],Arr[i]
                print(Arr)
        Arr[i+1], Arr[right] = Arr[right], Arr[i+1]
        return i+1
    def quickSort(self, Arr, left, right):
        if left < right:
            pivotIndex = self.partition(Arr, left, right)
            self.quickSort(Arr, left, pivotIndex-1)
            self.quickSort(Arr, pivotIndex+1, right)
        return Arr



if __name__ == "__main__":
    array = [15,38,29,10,78,8,-7,100,76,17]
    s = Solution()
    s.quickSort(array, 0, len(array)-1)
    print(array)