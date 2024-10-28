#6) Python Program to Get the Fibonacci Series of a Given Range:

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter the range: "))
fibonacci(num)
