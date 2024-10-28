#60) Python Program for a Sample String Letter Count:

sample_string = "w3SCHOOL"
letter_count = {char: sample_string.count(char) for char in sample_string}
print("Count of each letter:", letter_count)
