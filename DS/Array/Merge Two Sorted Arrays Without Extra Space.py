# declare 2 arrays
# both will be sorted
# needed two pointers
# one will iterate through 1st array other stay on 1st index of 2nd array
# if greater swap
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def SortArray(arr1, arr2):
    i = j = 0
    n = len(arr1)
    for i in range(n - 1):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = swap(arr1[i], arr2[0])
            arr2.sort()

arr1=[1,3,4,6,9]
arr2=[2,5,7,8,0]
SortArray(arr1,arr2)

print(arr1)
print(arr2)