#29) Python Function to Get the Largest Number, Smallest Number, and Sum of All Elements from a List:

def list_statistics(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    return largest, smallest, total

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
largest, smallest, total = list_statistics(numbers)
print("Largest:", largest, "Smallest:", smallest, "Sum:", total)
