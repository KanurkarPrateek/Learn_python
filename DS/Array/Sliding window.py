def getMaxSum(arr, k):
    maxSum = 0
    windowSum = 0
    start = 0

    for i in range(len(arr)):
        windowSum += arr[i]

        if ((i - start + 1) == k):
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1

    return maxSum

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Moving averages for window size", k, ":", moving_average(nums, k))
