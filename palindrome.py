#Write a Python program to print all palindromes in a line of text.

def is_palindrome(word):
    return word == word[::-1]

text = "madam racecar apple level noon"
palindromes = [word for word in text.split() if is_palindrome(word)]
print("Palindromes:", palindromes)  