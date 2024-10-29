#77) Python Program to Read a File Line by Line and Store in a Variable:

with open("example.txt", "r") as ex:
    content = ex.read()
print("File content:", content)
