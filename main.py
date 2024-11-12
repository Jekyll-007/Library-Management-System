class Library:
    def __init__(self, name, book_list):
        self.bookList = book_list 
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict[book] = user 
            print("Lender book database has been updated. You can take the book now.")
        else:
            print("Sorry, the book has been lent to someone else.", self.lendDict[book]) 

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added!")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print(f"The book '{book}' has been returned.")
        else:
            print("This book was not lent out.")

if __name__ == '__main__':
    library = Library("Let's Upskill", ['Python', 'Javascript', 'C++', 'C#', 'React', 'Tailwind', 'Social Skills', 'C+'])

    while True:
        print("\nWelcome to", library.name)
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Return a Book")
        print("4. Add a Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.displayBooks()

        elif choice == '2':
            user = input("Enter your name: ")
            book = input("Enter the name of the book you want to lend: ")
            library.lendBook(user, book)

        elif choice == '3':
            book = input("Enter the name of the book you want to return: ")
            library.returnBook(book)

        elif choice == '4':
            book = input("Enter the name of the new book you want to add: ")
            library.addBook(book)

        elif choice == '5':
            print("Thank you for using the library management system!")
            break

        else:
            print("Invalid choice! Please select a valid option.")