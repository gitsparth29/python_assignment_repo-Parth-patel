#74) Python Program to Read the First n Lines of a File:

def read_first_n_lines(filename, n):
    with open(filename, "r") as file:
        for i in range(n):
            print(file.readline().strip())

read_first_n_lines("example.txt", 5)
