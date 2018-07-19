def reverseSenstence(data):
    data = data[::-1]
    cache = data.split(" ")
    result = ""
    for item in cache:
        result += item[::-1] + " "
    return result

def leftRotateString(data, index):
    left = data[:index]
    right = data[index:]
    cache = left[::-1] + right[::-1]
    return cache[::-1]
    

if __name__ == "__main__":
    data = "I am a student"
    leftString = "I am a student"
    print(reverseSenstence(data))
    print(leftRotateString(leftString, 2))