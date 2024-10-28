#22) Python Function to Reverse a String if its Length is a Multiple of 4:

def reverse_if_multiple_of_4(string):
    if len(string) % 4 == 0:
        return string[::-1]
    return string

string = input("Enter a string: ")
print("Result:", reverse_if_multiple_of_4(string))
