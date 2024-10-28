#39) Python Program to Find the Second Smallest Number in a List:

def second_smallest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()
    return unique_lst[1] if len(unique_lst) >= 2 else None

lst = [1, 2, 3, 4, 5]
print("Second smallest number:", second_smallest(lst))
