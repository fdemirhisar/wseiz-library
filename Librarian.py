'from Person import Person\n\nclass Librarian(Person):' 
'    def __init__(self, name, person_id):' 
'        super().__init__(name, person_id)' 
'' 
'    def add_book(self, library, book):' 
'        library.add_book(book)' 
'' 
'    def remove_book(self, library, book):' 
'        library.remove_book(book)' 
'' 
'    def add_patron(self, library, patron):' 
'        library.add_patron(patron)' 
'' 
'    def remove_patron(self, library, patron):' 
'        library.remove_patron(patron)' 
'' 
'    def __str__(self):' 
'        return "Librarian: " + self.name + " (ID: " + self.person_id + ")"' 