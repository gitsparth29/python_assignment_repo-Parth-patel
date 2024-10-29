#89) Handling Exceptions with try/except/finally:try:

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print("You entered:", num)
finally:
    print("Execution completed.")
