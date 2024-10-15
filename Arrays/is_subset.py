def isSubset(arr1, arr2):
    # Convert both arrays to sets
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Check if all elements in set1 are in set2
    return set1.issubset(set2)

# Driver Code
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(isSubset(arr1, arr2))  # Output: True

arr3 = [1, 2, 9]
arr4 = [1, 2, 3, 4, 5, 6, 7, 8]
print(isSubset(arr3, arr4))  # Output: False
