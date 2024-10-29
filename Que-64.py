#64) Python Function to Check if a String is a Palindrome:

def s_palindrome(s):
    return s == s[::-1]
print("Is palindrome:", s_palindrome("mam"))
