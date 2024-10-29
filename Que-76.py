#76) Python Program to Read a File Line by Line and Store in a List:

with open("example.txt", "r") as ex:
    lines = [line.strip() for line in ex]
print("Lines as list:", lines)
