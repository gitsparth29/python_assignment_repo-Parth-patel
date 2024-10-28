#23) Python Program to Get a String Made of the First 2 and the Last 2 Characters of a Given String:

def first_and_last_2_chars(string):
    if len(string) < 2:
        return ""
    return string[:2] + string[-2:]

string = input("Enter a string: ")
print("Result:", first_and_last_2_chars(string))
