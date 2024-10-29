#81) 90)e python program that user to enter only odd numbers, else will raise an exception.

class OddError(Exception):
    pass

try:
    number = int(input("Enter an odd number: "))
    if number % 2 == 0:
        raise OddError("This is not an odd number!")
    print("You entered an odd number.")
except OddError as e:
    print(e)
