def firstNonRepeating(arr):
    n = len(arr)
    for i in range(n):
        is_repeating = False
        for j in range(n):
            if i != j and arr[i] == arr[j]:
                is_repeating = True
                break
        if not is_repeating:
            return arr[i]
    return -1  # Return -1 if no non-repeating element is found

# Example
arr = [9, 4, 9, 6, 7, 4]
print(firstNonRepeating(arr))  # Output: 6
