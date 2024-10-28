#57) Python Program to Find the Highest 3 Values in a Dictionary:

dictionary = {'a': 50, 'b': 100, 'c': 900, 'd': 40, 'e': 70}
top_3 = sorted(dictionary.values(), reverse=True)[:3]
print("Top 3 values:", top_3)
