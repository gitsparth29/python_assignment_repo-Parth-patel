#19) Python Program to Count the Occurrences of Each Word in a Given Sentence:
from collections import Counter
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = Counter(words)
print("Word occurrences:", word_count)
