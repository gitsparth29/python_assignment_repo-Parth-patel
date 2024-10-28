#52) How to Check the Presence of a Key in a Dictionary:
#•	To check if a key exists, use the in operator:

dictionary = {'a': 1, 'b': 2, 'c': 3}
key = 'a'
if key in dictionary:
    print("Key is present.")
else:
    print("Key is not present.")
