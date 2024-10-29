#73) Python Program to Append Text to a File and Display It:

with open("example.txt", "a") as ex:
    ex.write("Appended text.\n")

with open("example.txt", "r") as ex:
    print(ex.read())
