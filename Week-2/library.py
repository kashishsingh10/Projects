'''--------------------------------Library Management System---------------------------------'''
# CLASS BOOK
class Book:
    def __init__(self,author,id,title):
        self.author = author
        self.id = id
        self.title = title
        self.availablitity_status = True

#display data
    def get_data(self):
        print("Book author:",self.author)
        print("Book ID:",self.id)
        print("Book Title:",self.title)
        print("Availablitity Status:",self.availablitity_status)
        if self.availablitity_status:
            print("Book is Available")
        else:
            print("Book is Not Available")
# CLASS LIBRARY
class Library:
    def __init__(self):
        self.books={}
#ADD BOOK
    def add_book(self):
        id=int(input("Enter Book Id:"))
        if id in self.books:
            print("Already Exist")
        else:
            author=input("Enter Book Author:")
            title=input("Enter Book Title:")
            new_book=Book(author,id,title)
            self.books[id]=new_book
            print("Book Added Successfully")
#view books
    def view_books(self):
        if not self.books:
            print("Books Not Available")
        else:
            print("Books are ")
            for Book in self.books.values():
                Book.get_data()
#issue book
    def issue_book(self):
        id=int(input("Enter Book ID:"))
        if id not  in self.books:
            print("Book does not Exists")
        else:
            Book=self.books[id]      
            if Book.availablitity_status == False:
                print("Book is  already Issued")
            else:
                Book.availablitity_status=False
                print("Book is Issued")
#return book
    def return_book(self):
        id=int(input("Enter Book ID:"))
        if id not  in self.books:                
            print("Book does not Exists")
        else:
            Book=self.books[id]      
            if Book.availablitity_status == True:
                print("Book is  already There")
            else:
                Book.availablitity_status=True
                print("Book is Returned")
# Search book
    def search_book(self):
        id=int(input("Enter Book ID:"))
        if id in self.books:
            print("Book is found")
            self.books[id].get_data()
        else:
            print("Book does not Found")
#OBJECT OF CLASS LIBRARY
l1=Library()                   
while True:          
    print("--------OPTIONS---------\n 1.Add Book \n 2.View Book \n 3.issue Book") 
    print(" 4.Return Book \n 5.Search Book \n 6.Exit")

    choice=int(input("Enter Your Choice(1-6) : "))
    if (choice==1):
         l1.add_book()
    elif(choice==2):
         l1.view_books()
    elif(choice==3):
         l1.issue_book() 
    elif(choice==4):
         l1.return_book() 
    elif(choice==5):
         l1.search_book()      
    elif(choice==6):
        print("Thank you for using library management system \n Program Executed Successfully ")
        break
    else:
        print("Enter Valid Choice(1-6)")
        