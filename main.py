class Book:
    def __init__(self,tittle,author,is_borrowed=False):
        self.tittle=tittle
        self.author=author
        self.is_borrowed=is_borrowed
    def borrow(self):
        self.is_borrowed=True
        print(self.tittle,"is borrowed")
    def return_book(self):
        self.is_borrowed=False
        print(self.tittle,"is returned")
b1=Book("Alice In wonderland","Lewis Correl")
b2=Book("The Sage Who Reimagined Hinduism", "Shashi Tharoor")
b3=Book("Tides of Time: Bharat's History through Murals in Parliament","Sudha Murty")
b1.borrow()
b2.borrow()
b3.borrow()
b1.return_book()
b2.return_book()





        
