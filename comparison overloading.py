class Book:
    def __init__(self):
        title=""
        publisher=""
        price=0
    def set(self,title,publisher,price):
        self.title=title
        self.publisher=publisher
        self.price=price
    def display(self):
        print("Title:",self.title)
        print("Publisher:",self.publisher)
        print("Price:",self.price)
    def __gt__(self,B):
        if(self.price>B.price):
            return True
        else:
            return False
B1=Book()
B1.set("Pythonprogramming","Oxford University",525)
B2=Book()
B2.set("Let us see","BPB",300)
if(B1>B2):
    print("this book has more knowledge so i will buy")
    B1.display()
