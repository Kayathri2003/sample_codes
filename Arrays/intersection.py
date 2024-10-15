# a1=[1,2,2,3,4,5]
# a2=[2,4,5,6,7]
# a=[]
# for arr in a1:
#     if arr in a2:
#         a.append(arr)
# print(list(set(a)))


def findIntersection(arr1, arr2):
    # Convert both arrays to sets and find the intersection
    set1 = set(arr1)
    set2 = set(arr2)
    
    # The intersection of two sets will give the common elements
    intersection = set1.intersection(set2)
    
    return list(intersection)

# Driver code
arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]

result = findIntersection(arr1, arr2)
print("Intersection of the two arrays:", result)
