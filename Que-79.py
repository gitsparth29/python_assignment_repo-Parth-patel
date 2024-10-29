#79) Python Program to Count the Number of Lines in a Text File:

with open("example.txt", "r") as ex:
    line_count = sum(1 for line in ex)
print("Number of lines:", line_count)
