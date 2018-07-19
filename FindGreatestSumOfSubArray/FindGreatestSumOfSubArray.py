def findGreatestSumOfSubArray(numbers, length):
    nCurrentSum = 0
    nGreatestSum = 0
    for i in range(length):
        if nCurrentSum <= 0:
            nCurrentSum = numbers[i]
        else:
            nCurrentSum += numbers[i]
        
        if nCurrentSum > nGreatestSum:
            nGreatestSum = nCurrentSum
    return nGreatestSum

if __name__ == "__main__":
    numbers = [1, -2, 3, 10, -4, 7, 2, -5]
    length = len(numbers)
    print(findGreatestSumOfSubArray(numbers, length))