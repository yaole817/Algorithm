def isUglyNumber(number):
    while number % 2 == 0:
        number /= 2
    while number % 3 == 0:
        number /= 3
    while number % 5 == 0:
        number /= 5
    return number == 1
def getUglyNumber(uglyIndex):
    uglyNumber = [2, 3, 5]
    for i in range(uglyIndex):
        number = 


if __name__ == "__main__":
    