#35) Python Program to Generate and Print First and Last 5 Elements of Squares of Numbers from 1 to 30:

squares = [x**2 for x in range(1, 31)]
print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])

