def isPrime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0: return False
    return True

if __name__ == "__main__":
    import sys
    a = int(sys.argv[1])
    print(isPrime(a))
