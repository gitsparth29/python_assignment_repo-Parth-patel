#36) Python Function to Return a List with Unique Elements:

def unique_elements(lst):
    return list(set(lst))

lst = [1, 2, 2, 3, 4, 4, 5]
print("Unique elements:", unique_elements(lst))