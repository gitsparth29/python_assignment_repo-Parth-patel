#34) Python Function to Check if Two Lists Have at Least One Common Member:

def common_member(lst1, lst2):
    return any(item in lst1 for item in lst2)

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6]
print("Common member exists:", common_member(list1, list2))
