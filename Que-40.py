#40) Python Program to Get Unique Values from a List:

def unique_values(lst):
    return list(set(lst))

lst = [1, 2, 2, 3, 4, 4, 5]
print("Unique values:", unique_values(lst))
