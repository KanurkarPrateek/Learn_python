def SubArray( arr1 , arr2):
    setarr2 = set(arr2)

    for element in arr1:
        if element not in setarr2:
            return False
    return True

arr1 = [1, 5 , 4 , 9]
arr2 = [1,2,3,4,5,6,7,8]

print(SubArray(arr1,arr2))
