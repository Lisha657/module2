# Describe the concept of recursive function in Python with a suitable example.
#A recursive function is a function that calls itself to solve smaller instances of a problem until a base case is met.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
