#16) Python Program to Count the Frequency of Characters in a String:
from collections import Counter
string = input("Enter a string: ")
frequency = Counter(string)
print("Character Frequency:", frequency)
