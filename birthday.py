#Write a Python program that asks the user to enter a name, and the program displays the birthday of that person.
birthdays = {"Alice": "01-01-2000", "Bob": "15-06-1998", "Charlie": "20-12-1995"}

name = input("Enter a name: ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}.")
else:
    print("Name not found")