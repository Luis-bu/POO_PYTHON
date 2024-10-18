class Book():
    def __init__(self, title, author, pages):
        self.title=title
        self.author=author
        self.pages=pages
        self.available=True
    
    def __str__(self):
        return f"Titulo: {self.title}, autor: {self.author}, paginas: {self.pages}, disponible: {self.available}"
    
    def borrow(self):
        if self.available:
            self.available=False
            print("libro prestado exitosamente")
        
        else:
            print("Libro no disponible")    
    
    def return_book(self):
        if not self.available:
            self.available=True
            print("Libro devuelto exitosamente")
        
        else: print("Ya tenemos ese libro")
        
book1= Book("Think and become rich", "Napoleon Hill", 230)

book1.borrow()
book1.borrow()
book1.return_book()
print(book1)