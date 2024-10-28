#20) Python Program to Get a Single String from Two Given Strings, Swapping the First Two Characters of Each:
def swap_and_combine(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + " " + new_str2

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Combined string:", swap_and_combine(str1, str2))
