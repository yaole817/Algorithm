# N = 1000
# results = [(0, 0), (1, 1)]
# for i in range(2, N+1):
#     minNum, minPos = N + 1, -1
#     for j in range(1, i + 1):
#         temp = 1 + max(j - 1, results[i - j][0])
#         if temp < minNum:
#             minNum, minPos = temp, j
#     results.append((minNum, minPos))
# for result in results:
#     print(result)

def f(n):
    if n == 1:      #把所有的边界问题找到
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 1
    if n == 4:
        return 3
    if n == 5:
        return 1

    h = [1,3,5]
    minx = n
    for i in range(3):
        coun = f(n-h[i])+1    # 采用了递归的思想 这里是从上到下，
        if minx > coun:       # 复杂度比较高
            minx = coun
    return minx

print(f(11))