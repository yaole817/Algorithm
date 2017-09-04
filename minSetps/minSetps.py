
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(2,int(n)):
            if n % i == 0:
                return self.minSteps(n/i) + i
        return n

if __name__ == '__main__':
	s = Solution()
	print(s.minSteps(1000))