#82) Python Program to Copy the Contents of a File to Another File:

with open("example1.txt", "r") as source, open("example2.txt", "w") as dest:
    dest.write(source.read())
