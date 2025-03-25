# Bookstore Management System (CLI)

## Overview
This is a **Command Line Interface (CLI) Bookstore Management System** written in Python. It allows users to manage books in a store by adding, viewing, and removing books while persisting data in a JSON file.

## Features
- **Add Books**: Enter book details (Title, Author, ISBN, Genre, Price, Quantity) and store them.
- **Prevent Duplicates**: Ensures unique ISBN for each book.
- **View Books**: Displays all books in a structured format.
- **Remove Books**: Deletes a book using its ISBN.
- **Persistent Storage**: Saves book data in `books.json` for future sessions.
- **Interactive Menu**: Simple menu-driven interface.

## Project Structure
```
Bookstore-CLI/
│── books.json                # Stores book data
│── main.py                   # Entry point of the application
│── bookstore.py              # Contains the BookStore class
│── README.md                 # Project documentation
```

## Installation & Usage
### Prerequisites
- Python 3.x installed on your system.

### Steps to Run the Program
1. **Clone the Repository** (if hosted on GitHub):
   ```sh
   git clone https://github.com/ahad2343L/Bookstore-CLI.git
   cd Bookstore-CLI
   ```
2. **Run the program:**
   ```sh
   python main.py
   ```
3. **Follow the menu options:**
   - Add new books
   - View stored books
   - Remove books
   - Exit the application

## Example Usage
```
Book Store Management System
1. Add Book
2. View Books
3. Remove Book
4. Exit
Choose an option: 1

Enter book title: The Alchemist
Enter author name: Paulo Coelho
Enter ISBN: 9780062315007
Enter genre: Fiction
Enter price: 12.99
Enter quantity: 5
Book added successfully!
```

## Notes
- The `books.json` file is created automatically and updated whenever changes occur.
- The program validates inputs (e.g., price must be positive, quantity must be non-negative).
- The user cannot add a book with an already existing ISBN.

## License
This project is open-source and free to use.

## Author
Developed by Abdul Ahad.
