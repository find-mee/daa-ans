def selection(arr):
    n= len(arr)
    for i in range(n-1):
        min =i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min =j
        if min!=i:
            arr[i],arr[min] = arr[min],arr[i]

arr = []
ele = int(input("Enter num of eles "))

print("Enter elems")
for i in range(ele):
    elem = int(input())
    arr.append(elem)

selection(arr)

print(arr)