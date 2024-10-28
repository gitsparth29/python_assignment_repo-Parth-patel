#28) Differentiate Between append() and extend() Methods?
#•	append(): Adds a single element to the end of a list.
list1 = [1, 2, 3]
#list1.append([4, 5])
#print(list1)
# list1 becomes [1, 2, 3, [4, 5]]
#•	extend(): Adds each element of an iterable (e.g., list) to the end of the list.
#list1 = [1, 2, 3]
list1.extend([4, 5])
print(list1)
# list1 becomes [1, 2, 3, 4, 5]
