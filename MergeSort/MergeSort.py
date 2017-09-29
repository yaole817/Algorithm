
class Solution(object):
    def merge(self,A1,A2):
        i,j = 0,0
        result = []
        while i < len(A1) and j < len(A2):
            if A1[i] <= A2[j]:
                result.append(A1[i])
                i += 1
            else:
                result.append(A2[j])
                j += 1
        result += A1[i:] + A2[j:]
        return result

    def mergeSort(self,A):
        if len(A) <= 1:
            return A
        halfNum = len(A)//2
        left = self.mergeSort(A[:halfNum])
        right = self.mergeSort(A[halfNum:])
        return self.merge(left,right)


if __name__ == "__main__":
    array = [15,38,29,10,78,8,-7,100,76,-19]
    s = Solution()
    print(s.mergeSort(array))
