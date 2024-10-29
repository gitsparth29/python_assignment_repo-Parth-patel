#81) Python Program to Write a List to a File:

lines = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w") as file:
    file.write("\n".join(lines))
