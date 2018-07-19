class LastNumOfCircle():
    def __init__(self, N, m):
        array = [i for i in range(N)]
        while len(array) > 1:
            self.delteMnum(array, m)
        print(array)
    def delteMnum(self, array, M):
        for i in range(M - 1):
            num = array.pop()
            array.insert(0, num)
        array.pop()

def lastRemaining(n, m):
    if n < 1 or m < 1:
        return -1
    last = 0
    for i in range(2, n +1):
        last = (last + m) % i
    return last 

def lastRemaining1(n, m):
    if n is 1: return 0
    return (lastRemaining1(n - 1, m) + m) % n


if __name__ == "__main__":
    # lastNumOfCircle = LastNumOfCircle(90000, 7)
    last = lastRemaining(900, 7)
    print(lastRemaining1(900, 7))
    print(last)



