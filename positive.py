# Write a Python program to read n integers into a list and separate the positive and negative numbers into two different lists.

numbers = [3, -2, 5, -7, 8, -1]
positive = [num for num in numbers if num > 0]
negative = [num for num in numbers if num < 0]

print("Positive Numbers:", positive)
print("Negative Numbers:", negative)