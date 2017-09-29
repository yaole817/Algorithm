class Solution(object):
    def judgePrimerNumber(self, n):
        if n < 2 : return False
        for j in range(2, int(n**0.5)+1):
            if n % j == 0 : return False
        return True

    def generatePrimerNumber(self,n):
        return [j for j in range(1, n+1) if self.judgePrimerNumber(j)]


class Solution1(object):
    def __init__(self):
        self.primer = [2,3,5]

    def judgePrimerNumber(self, n):
        if n < 2 : return False
        for i in self.primer:
            if n % i == 0: return False
        return True

    def generatePrimerNumber(self,n):
        for i in range(1, n+1):
            if self.judgePrimerNumber(i):
                if i > self.primer[-1]:
                    self.primer.append(i)
                yield i
            
        
if __name__ == "__main__":
    import timeit
    num = 1000000
    s = Solution()
    start = timeit.default_timer()
    a = s.generatePrimerNumber(num)
    a = list(a)
    end = timeit.default_timer()
    print(a)

    print((end - start))

