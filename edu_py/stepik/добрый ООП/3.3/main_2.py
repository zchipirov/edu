import sys


class Book:
    def __init__(self, title, author, pages) -> None:
        self.__title = title
        self.__author = author
        self.__pages = pages
        
    def __str__(self) -> str:
        return f"Книга: {self.__title}; {self.__author}; {self.__pages}"
    

lst_in = list(map(str.strip, sys.stdin.readlines()))
books = Book(lst_in[0], lst_in[1], lst_in[2])
print(books)