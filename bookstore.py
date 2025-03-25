import json
import os

BOOKS_FILE = "books.json"

class BookStore:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r") as file:
                return json.load(file)
        return []

    def save_books(self):
        with open(BOOKS_FILE, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        genre = input("Enter genre: ")
        price = input("Enter price: ")
        quantity = input("Enter quantity: ")
        
        if any(book["ISBN"] == isbn for book in self.books):
            print("Error: A book with this ISBN already exists.")
            return
        
        book = {
            "Title": title,
            "Author": author,
            "ISBN": isbn,
            "Genre": genre,
            "Price": float(price),
            "Quantity": int(quantity)
        }
        self.books.append(book)
        self.save_books()
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Genre: {book['Genre']}, Price: {book['Price']}, Stock: {book['Quantity']}")

    def remove_book(self):
        isbn = input("Enter ISBN of book to remove: ")
        self.books = [book for book in self.books if book["ISBN"] != isbn]
        self.save_books()
        print("Book removed successfully!")

    def menu(self):
        while True:
            print("\nBook Store Management System")
            print("1. Add Book")
            print("2. View Books")
            print("3. Remove Book")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.remove_book()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid option. Try again.")

