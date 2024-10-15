def second_largest(arr):
    if len(arr)<2:
        return "Array should have at least 2 numbers"
    arr.sort(reverse=True)
    for i in range (1,len(arr)):
        if arr[i] < arr[i-1]:
            return arr[i]
    return "No second largest element"

#Test cases
print(second_largest([1,2,3,4,5]))
print(second_largest([4,2,1,5,3]))