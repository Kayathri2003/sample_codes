def mergeSortedArrays(arr1, arr2):
    # Initialize pointers for both arrays
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    merged = []  # Resultant merged array

    # Traverse both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    return list(set(merged))

# Driver code
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 5, 8]
print("Merged array:", mergeSortedArrays(arr1, arr2))