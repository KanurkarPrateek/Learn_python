def missingNum(arr):
    n = len(arr)
    expectedSum = ((n+2)*(n+1))//2
    actualSum = sum(arr)
    diff = expectedSum - actualSum
    return diff

arr = list(map(int,input("Enter an array").split()))
missNum = missingNum(arr)
print(missNum)
