def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        
        arr[j+1]=temp

arr = []
ele = int(input("Enter num of eles "))

print("Enter elems")
for i in range(ele):
    elem = int(input())
    arr.append(elem)

insertion(arr)

print(arr)