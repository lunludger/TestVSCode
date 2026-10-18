# This program handles inventory book
# Declare inventory list as a global variable so it can be assessed by all methods

import sqlite3

conn = sqlite3.connect("ebookstore.db")
cursor = conn.cursor()


inventory = []
# Add book a new book to the database
def add_book():

    title = input(" Enter the book title: ")
    authorID = input(" Enter the authorID of the book: ")
    qty = int(input(" Enter the quantity of books required: "))
    name = input(" Enter the name of the book: ")
    country = input(" Enter the country of the book: ")

    book = {'id': id,
            'title' : title,
            'authorID' : authorID,
            'qty' : qty,
            'name' : name,
            'country' : country
           }

    inventory.append(book)
    print(f"{id}, {title}, {authorID}, {qty}, {name}, {country}")

# Update book information
def update_book():
    if not inventory:
        print("Inventory is empty.\n")
        return

    try:
        id = (input("Enter the id of the book you want to update: ")) - 1
        if 0 <= id < len(inventory):
            book = inventory[id]
            updated_book_id = input(f"New id ({book['id']}): ")
            updated_book_title = input(f"New title ({book['title']}): ")
            updated_book_authorID = input(f"New authorID ({book['authorID']}): ")
            updated_book_qty = int(input(f"New qty ({book['qty']}): "))
            updated_book_name = input(f"New name ({book['name']})")
            updated_book_country = input(f"New country ({book['country']})")

            book["id"] = updated_book_id
            book["title"] = updated_book_title
            book["authorID"] = updated_book_authorID
            book["qty"] = updated_book_qty
            book["book"] = updated_book_name
            book["country"] = updated_book_country
            print("Book updated!\n")

        else:
            print("Wrong option selection.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Delete books from the database
def delete_book():
    try:
        id = input("Enter book id to delete: ")
        if 0 <= id < len(inventory):
            removed = inventory.pop(id)
            print(f"Removed: {removed['id']}\n")
        else:
            print("Wrong option selection.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to search the database to find a specific book
def search_book():
    title_search = input("Enter title to search: ").lower()
    found = False

    for book in inventory:
        if title_search in book["title"].lower():
            print(f"Found: {book['id']} {book['title']} {book['authorID']} {book['qty']} {book['name']} {book['counrty']}")
            found = True

    if not found:
        print("No matching book found.")
    print()

# Function to view all books in the database
def view_all_books():
    books = []
    for book in books:
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("AuthorID:", book["authorID"])
        print("qty:", book["qty"])
        print("name:", book["name"])
        print("country:", book["country"])

# Menu to select options from 1 to 6

def main():
    print("Welcome to the eBook Store")

def menu():
    while True:
        print("\n===== eBook Store =====")
        print("1. Enter Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. Display Books")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            update_book()

        elif choice == "3":
             delete_book()

        elif choice == "4":
             search_book()

        elif choice == "5":
             view_all_books()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
    menu()




