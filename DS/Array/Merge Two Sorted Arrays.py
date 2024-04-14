def MergedArr(arr1 , arr2):
    merged=[]
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i]<arr2[j]:
            merged.append(arr1[i])
            i += 1
        elif arr1[i]>arr2[j]:
            merged.append(arr2[j])
            j += 1
        else:
            # Append the element from either array if they are equal
            merged.append(arr1[i])
            i += 1
            j += 1

    # remaining array

    while i < len(arr1):
        merged.append(arr1[i])
        i +=1
    while j < len(arr2):
        merged.append(arr2[j])
        j +=1

    return merged

array1 = list(map(int,input("enter the array 1").split()))
array2 = list(map(int,input("enter the array 2").split()))

Mergedarray = MergedArr(array1,array2)

print(Mergedarray)