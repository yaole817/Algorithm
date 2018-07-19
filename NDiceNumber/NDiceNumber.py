MAX_VALUE = 6
class Solution1():
    def __init__(self, N):
        self.__N = N
    def printProbability(self, number):
        if number < 1: return
        maxSum = number * MAX_VALUE

        for i in range(number, maxSum + 1):
            ratio = p



