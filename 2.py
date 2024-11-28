books = []

def add_book(title, author):
    books.append({"title": title, "author": author, "borrowed": False})

def borrow_book(title):
    for book in books:
        if book["title"] == title and not book["borrowed"]:
            book["borrowed"] = True
            return f"You borrowed {title}."
    return "Book not available."

def return_book(title):
    for book in books:
        if book["title"] == title and book["borrowed"]:
            book["borrowed"] = False
            return f"You returned {title}."
    return "Book not found or not borrowed."

def list_books():
    for book in books:
        status = "Borrowed" if book["borrowed"] else "Available"
        print(f"{book['title']} by {book['author']} - {status}")

# 실행
while True:
    print("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. List Books\n5. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        add_book(title, author)
    elif choice == 2:
        title = input("Enter book title to borrow: ")
        print(borrow_book(title))
    elif choice == 3:
        title = input("Enter book title to return: ")
        print(return_book(title))
    elif choice == 4:
        list_books()
    elif choice == 5:
        break
