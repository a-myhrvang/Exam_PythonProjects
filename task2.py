class Book:
    def __init__(self, title, author, num_pages):
        # Initializes a book with title, author, number of pages and its checkout status
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.is_checked_out = False
        
    def __str__(self):
        # Returns a string representation of the book, including status
        status = "Checked out" if self.is_checked_out else "Available"
        return f'"{self.title}" by {self.author}, {self.num_pages} pages [{status}]'



class Library:
    def __init__(self):
        # Initializes an empty list to store books
        self.books = []
        
    def add_book(self, book):
        # Adds a book to the library if not already present
        if any(b.title.lower() == book.title.lower() for b in self.books):
            print(f'Book "{book.title}" already exists in the library.')
            return
        self.books.append(book)
        print(f'Added: {book.title}')

        
    def remove_book(self, title):
        # Removes a book based on title (if found)
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'Removed: {title}')
                return
        print(f'Book "{title}" not found.')
        
    def check_out(self, title):
        # Marks a book as checked out if available
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_checked_out:
                    print(f'Book "{title}" is already checked out.')
                else:
                    book.is_checked_out = True
                    print(f'Book "{title}" has been checked out.')
                return
        print(f'Book "{title}" not found.')
        
    def check_in(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_checked_out:
                    print(f'Book "{title}" was not checked out.')
                else:
                    book.is_checked_out = False
                    print(f'Book "{title}" has been returned.')
                return
        print(f'Book "{title}" not found.')
        
    def list_books(self):
        # Prints all books in the library
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                print(book)
                
                
# Main program for testing Library and Book functionality
if __name__ == "__main__":
    print("\n –––| Library Management System |–––\n")
    
    # Create library
    my_library = Library()
    
    # Add books
    book1 = Book("1984", "George Orwell", 328)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    
    print("\n –––| Initial book list |–––")
    my_library.list_books()
    
    # Try to borrow a book
    print("\n –––| Checking out '1984' |–––")
    my_library.check_out("1984")
    
    # Try to return a book
    print("\n –––| Checking in '1984' |–––")
    my_library.check_in("1984")
    
    # Try to remove a book
    print("\n –––| Removing 'To Kill a Mockingbird' |–––")
    my_library.remove_book("To Kill a Mockingbird")
    
    # Show endresult
    print("\n –––| Final book list |–––")
    my_library.list_books()