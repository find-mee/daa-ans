def merge(arr):
    if len(arr)<=1:
        return arr, 0

    mid = len(arr)//2
    left, inversions_left = merge(arr[:mid])
    right, inversions_right = merge(arr[mid:])
    merged, inversions_merge = mergeSort(left, right)

    return merged, inversions_left + inversions_right + inversions_merge


def mergeSort(left,right):
    inversions = 0
    i,j = 0,0
    merged=[]
    
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            inversions += len(left) - i
            merged.append(right[j])
            j+=1
        else:
            merged.append(left[i])
            i+=1

    while i<len(left):
        merged.append(left[i])
        i+=1

    while j<len(right):
        merged.append(right[j])
        j+=1

    return merged, inversions

playlist_num = [2,3,1,5,8,4,7,6]
inversions = 0

playlist_num, inversions = merge(playlist_num)

print("sorted playlist ", playlist_num)
print("inversions ", inversions)