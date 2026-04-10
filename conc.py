class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author self.price = price
 
    def show_books(self):
        print("\nThe name of the book is: ",self.title)
        print("The name of the author is: ",self.author)
        print("The price of the book is: ",self.price)
        
name = str(input("Enter the name of the book: "))
author = str(input("Enter the name of the author: "))
price = str(input("Enter the price of the book: "))

book1 = Book(name,author,price)
book1.show_books()
