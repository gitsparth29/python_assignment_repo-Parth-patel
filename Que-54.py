#54) Python Program to Check if Multiple Keys Exist in a Dictionary:

dictionary = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'b']
if all(key in dictionary for key in keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys are present.")
