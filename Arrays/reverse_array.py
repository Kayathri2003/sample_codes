arr=[1,2,3,4,5,6,7]
# arr=arr[::-1]
# print(arr)

# arr.reverse()
# print(arr)

i=0
s=len(arr)
while i<s//2:
    arr[i],arr[s-i-1]=arr[s-i-1],arr[i]
    i+=1
print(arr)
    
