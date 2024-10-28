#21) Python Program to Add 'ing' or 'ly' to a Given String Based on Certain Conditions:def add_suffix(string):
    if len(string) >= 3:
        if string.endswith('ing'):
            return string + 'ly'
        else:
            return string + 'ing'
    return string

string = input("Enter a string: ")
print("Modified string:", add_suffix(string))
