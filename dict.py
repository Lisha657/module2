# Create a Python program that uses a dictionary to store the names and ages of people. Ask the user to enter a name, and the program should display the age of that person.
people = {"Alice": 25, "Bob": 30, "Charlie": 22}

name = input("Enter a name: ")
if name in people:
    print(f"{name} is {people[name]} years old.")
else:
    print("Name not found.")