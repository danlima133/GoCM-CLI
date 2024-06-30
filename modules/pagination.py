from  modules.console import console
from interfaces.InterfaceReadBook import InterfaceReadBook

class Book():
    def __init__(self, itens:list, itens_per_page:int = 3):
        self.__book = {}
        self.__itens_per_page = itens_per_page

        self.__pages:list
        
        for count, iten in enumerate(itens):
            factor_counter = count % self.__itens_per_page
            page = int(count / self.__itens_per_page) + 1
            if factor_counter == 0:
                if self.__book.get(page, None) == None:
                    self.__book[page] = []
                self.__book[page].append(iten)
            else:
                self.__book[page].append(iten)
        
        self.__pages = self.__book.keys()
    
    def get_book(self):
        return self.__book
    
    def get_pages(self):
        return self.__pages

class BrowseBook():
    def __init__(self, reader):
        self.reader = reader
    
    def start(self):
        while True:
            user_input = console().input(f"Choice Page Book: pages: {self.reader.book.get_pages()}: ")
            if user_input in ["q", "Q", "Quit", "quit", "Exit", "exit"]:
                break
            else:
                try:
                    page = int(user_input)
                except Exception:
                    console().print("This not number")
                    continue
                self.reader.read(page)

class ReaderHelpBook(InterfaceReadBook):
    def __init__(self, book):
        super().__init__(book)
    
    def read(self, page = 0):
        if page <= 0:
            for p in self.book.get_pages():
                console().rule(f"Page {p}")
                for iten in self.book.get_book()[p]:
                    console().print(iten)
        else:
            try:
                itens = self.book.get_book()[page]
                console().rule(f"Page {page}")
                for iten in itens:
                    console().print(iten)
            except Exception:
                console().print(":warning: [red]Page Not Found[/red]")