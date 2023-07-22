def isUnique(list):
    if len(list) == len(set(list)):
        return True
    return False

list1 = [1,2,34,5]
list2 = [1,2,3,5,5]
print("List 1 is")
if isUnique(list1):
    print("unique")
else:
    print("not unique")
print("List 2 is")
if isUnique(list2):
    print("unique")
else:
    print("not unique")

