#80) Python Program to Count the Frequency of Words in a File:

from collections import (Counter)
with open("example.txt", "r") as ex:
    words = ex.read().split()
    word_count = Counter(words)
print("Word frequency:", word_count)
