#Write a Python program to count how many times each character appears in a given string and store the count in a dictionary.
def count_chars(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(count_chars("hello world"))