#32) Python Program to Remove Duplicates from a List:

def remove_duplicates(lst):
    return list(set(lst))

lst = [1, 2, 2, 3, 4, 4, 5]
print("List without duplicates:", remove_duplicates(lst))
