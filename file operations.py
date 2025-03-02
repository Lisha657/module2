
#Explain how to read numeric values from a file, perform some operations, and then write the results back to the file.

with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

total = sum(numbers)
mean = total / len(numbers)

with open('results.txt', 'w') as file:
    file.write(f"Sum: {total}\nMean: {mean}\n")