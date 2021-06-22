def subSum(arr, n, sum):
    sub = ([[False for i in range(sum + 1)]
            for i in range(n + 1)])
    for i in range(n + 1):
        sub[i][0] = True
    for i in range(1, sum + 1):
        sub[0][i] = False

    for i in range(1, n+1):
        for j in range(1, sum + 1):
            if arr[i-1] <= j:
                sub[i][j] = sub[i][j-arr[i-1]] or sub[i-1][j]
            else:
                sub[i][j] = sub[i-1][j]

    return sub[n][sum]


if __name__ == '__main__':
    arr = [1, 2, 3, 8, 12]
    sum = 11
    n = len(arr)
    if (subSum(arr, n, sum) == True):
        print("true")
    else:
        print("false")
