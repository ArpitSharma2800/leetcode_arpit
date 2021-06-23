from typing import List


def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    sum = 0
    for i in nums:
        sum = sum + i
    print(sum % 2)
    if (sum % 2) == 0:
        if(partition(nums, n, int(sum/2)) == True):
            return(True)
        else:
            return(False)
    else:
        return(False)


def partition(arr, n, sum):
    sub = ([[False for i in range(sum + 1)]
            for i in range(n + 1)])
    for i in range(n + 1):
        sub[i][0] = True
    for i in range(1, sum + 1):
        sub[0][i] = False

    for i in range(1, n+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                sub[i][j] = sub[i-1][j-arr[i-1]] or sub[i-1][j]
            else:
                sub[i][j] = sub[i-1][j]
    return sub[n][sum]


if __name__ == '__main__':
    arr = [1, 5, 11, 5]
    if (canPartition(arr) == True):
        print("true")
    else:
        print("false")
