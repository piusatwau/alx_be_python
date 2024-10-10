class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        pass
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    def __del__(self):
        return f"Deleting {self.title}"
    
book1 = Book("Poor Dad Rich Dad", "Robert Kiyosaki", 2013)
print(book1.__del__())
print(book1.__repr__())