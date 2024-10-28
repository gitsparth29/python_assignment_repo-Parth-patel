#24) Python Function to Insert a String in the Middle of Another String:

def insert_middle(main_string, insert_string):
    middle = len(main_string) // 2
    return main_string[:middle] + insert_string + main_string[middle:]

main_string = input("Enter the main string: ")
insert_string = input("Enter the string to insert: ")
print("Result:", insert_middle(main_string, insert_string))
