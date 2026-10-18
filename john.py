# Prompt the user to enter their name and convert it to lowercase
name = input("Enter your name").lower()

# Initialise an empty list to store incorrect names
incorrect_names = []

# Continue the loop until the user enters the correct name 'john'
while name != 'John':
    # Add the incorrect name to the list
    incorrect_names.append(name)
    # Prompt the user to enter their name again and convert to lowercase
    name = input("Enter your name ").lower()

# Print the list of incorrect names
 print(f"Incorrect names {incorrect_names}")