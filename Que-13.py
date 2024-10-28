#13) Python Program That Returns True if Two Given Integer Values are Equal or Their Sum or Difference is 5:

def check_values (a, b):
    return a == b or abs(a - b) == 5 or (a + b) == 5

print(check_values(5, 10))  # Example usage
