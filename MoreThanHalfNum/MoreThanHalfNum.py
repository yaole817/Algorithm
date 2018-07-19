def checkMoreThanHalgNum(numbers, length, number):
    times = 0
    for i in range(length):
        if numbers[i] == number:
            times += 1
    if times * 2 < length:
        return False
    return True

def moreThanHalfNum(numbers, length):
    result = numbers[0]
    times = 1
    for i in range(1, length):
        if times == 0:
            result = numbers[i]
            times = 1
        elif numbers[i] == result:
            times += 1
        else:
            times -= 1
    if not checkMoreThanHalgNum(numbers, length, result):
        return -1
    return result


if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2, 5, 4,5, 4, 5, 4,]
    result = moreThanHalfNum(numbers, len(numbers) - 1)
    print(result)