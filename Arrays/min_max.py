arr=[1,2,3,4,5,6,7]
# mini=min(arr)
# maxi=max(arr)
# print(mini,maxi)

def find_min_max_optimal(arr, low, high):
    # If there is only one element
    if low == high:
        return arr[low], arr[low]
    
    # If there are two elements
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    # If there are more than two elements, divide the array
    else:
        mid = (low + high) // 2
        min1, max1 = find_min_max_optimal(arr, low, mid)
        min2, max2 = find_min_max_optimal(arr, mid + 1, high)
        
        return min(min1, min2), max(max1, max2)

# Example usage:
arr = [5, 7, 1, 9, 3, 6, 8, 2, 4]
n = len(arr)
min_element, max_element = find_min_max_optimal(arr, 0, n - 1)
print(f"Optimal: Minimum element is {min_element}, Maximum element is {max_element}")
