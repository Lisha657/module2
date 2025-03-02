#Write a Python program to compute the mean, median, and mode of a list of numbers.

from statistics import mean, median, mode

numbers = [1, 2, 3, 3, 4, 5, 5, 5]

print("Mean:", mean(numbers))
print("Median:", median(numbers))
print("Mode:", mode(numbers))