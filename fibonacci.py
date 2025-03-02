
#Write a Python program to print Fibonacci sequence using a list.

n = int(input("Enter number of terms: "))
fib_sequence = []

fib_sequence.append(0)
if n > 1:
    fib_sequence.append(1)

for i in range(2, n):
    next_term = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_term)

print("Fibonacci series: ", fib_sequence)