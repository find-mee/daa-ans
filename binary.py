def binarySearch(arr, k):
    s=0; e=len(arr)-1; 
    while s<=e:
        m= (s+e)//2
        if arr[m]==k:
            return m
        elif arr[m]>k:
            e = m-1
        else:
            s = m+1
    return -1


arr = []
ele = int(input("Enter num of eles "))

print("Enter elems")
for i in range(ele):
    elem = int(input())
    arr.append(elem)

k = int(input("Enter key"))

ans = binarySearch(arr,k )

print(ans)


