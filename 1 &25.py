#Write a user-defined function to generate even numbers between 1 and 25.
def even_numbers():
    return [x for x in range(1, 26) if x % 2 == 0]

print(even_numbers()) 