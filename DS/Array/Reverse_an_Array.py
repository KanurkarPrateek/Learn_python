
arr = list(map(int,input("enter an array").split()))
n = len(arr)
i = 0
j = n-1


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a,b

while i < j:
    arr[i],arr[j]= swap(arr[i],arr[j])
    i = i+1
    j = j-1

print(arr)