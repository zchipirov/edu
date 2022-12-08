class Desc:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    
class Book:
    title = Desc()
    author = Desc()
    year = Desc()
    
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year
        

class Lib:
    def __init__(self) -> None:
        self.book_list = []
        
    def __len__(self):
        return len(self.book_list)
    
    def __add__(self, other):
        if not isinstance(other, Book):
            raise TypeError("Неверный тип данных")
        
        self.book_list.append(other)
        return self
    
    def __iadd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if type(other) not in (int, Book):
            raise TypeError("Неверный тип данных")
        
        if isinstance(other, Book):
            self.book_list.remove(other)
        elif isinstance(other, int):
            del self.book_list[other]
        return self
    
    def __isub__(self, other):
        return self.__sub__(other)
    
    