from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def calculate_late_fee(self,days):
        pass

class PhysicalBook(Book):
    def __init__(self, title, author, ISBN, is_available):
        super().__init__(title, author, ISBN)
        self.is_available = is_available
        
    def calculate_late_fee(self,days):
        late_fee = days * 1
        return late_fee  
    
    def get_info(self):
        print(f"Book Title : {self.title}")
        print(f"Book Author : {self.author}")
        print(f"Book ISBN : {self.ISBN}")
        print(f"Available : {self.is_available}")

class EBook(Book):
    def __init__(self, title, author, ISBN, file_size):
        super().__init__(title, author, ISBN)
        self.file_size = file_size
    
    def calculate_late_fee(self, days):
        late_fee = days * 0.5
        return late_fee
    
    def get_info(self):
        print(f"Book Title : {self.title}")
        print(f"Book Author : {self.author}")
        print(f"Book ISBN : {self.ISBN}")
        print(f"File Size : {self.file_size} MB")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def list_all_books(self):
        for book in self.books:
            book.get_info()
            print()
    
    def calculate_total_fees(self, days):
        total = 0
        for book in self.books:
            total += book.calculate_late_fee(days)
        return total
    
# Test
library = Library()
physical = PhysicalBook("Python 101", "John Doe", "123456", True)
ebook = EBook("Learn OOP", "Jane Smith", "789012", 50)

library.add_book(physical)
library.add_book(ebook)

library.list_all_books()

total_fees = library.calculate_total_fees(5)  # 5 days late
print(f"Total Late Fees (5 days): ${total_fees}")