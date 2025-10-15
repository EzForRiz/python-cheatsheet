book1 = ("1984", "Available", "George Orwell")
book2 = ("The Hobbit", "Checked Out", "J.R.R. Tolkien")

for book in library:
    print("Title:", book[0], "| Status:", book[1], "| Author:", book[2])




def borrow_book_tuple(library, title):
    # Loop through the library (list of books), with `i` as the index and `book` as the tuple containing book details
    for i, book in enumerate(library):
        # Check if the title of the current book matches the requested title
        if book[0] == title:
            # If the book is found, check if it is available (book[1] represents the status)
            if book[1] == "Available":
                # If the book is available, update its status to "Checked Out"
                # A new tuple is created, as tuples are immutable
                library[i] = (book[0], "Checked Out", book[2], book[3])
                print(title, "borrowed successfully.")  # Print confirmation message
            else:
                # If the book is already checked out (not available), print that it's already borrowed
                print(title, "already borrowed.")
            return  # Exit the function once the book has been found and processed
    # If the book with the given title is not found in the library, print a message
    print(title, "not found in library.")