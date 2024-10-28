#48) Python Script to Sort a Dictionary by Value (Ascending and Descending):
dictionary = {'a': 3, 'b': 1, 'c': 2}
# Ascending order
sorted_asc = dict(sorted(dictionary.items(), key=lambda item: item[1]))
print("Ascending:", sorted_asc)
# Descending order
sorted_desc = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)
