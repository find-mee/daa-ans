def linear(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
    return -1

arr = []
ele = int(input("Enter num of eles "))

print("Enter elems")
for i in range(ele):
    elem = int(input())
    arr.append(elem)

k = int(input("Enter key"))

ans = linear(arr,k )

print(ans)