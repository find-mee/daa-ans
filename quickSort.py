def quicksort(nums):
    length = len(nums)
    if length <=1:
        return nums
    pivot = nums[0]
    right=[]
    left = []
    
    for num in nums[1:]:
        if pivot> num:
            left.append(num)
        else:
            right.append(num)
    
    return quicksort(left) + [pivot] + quicksort(right)


numbers = [8, 3, 1, 7, 5, 6, 4, 2]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)

