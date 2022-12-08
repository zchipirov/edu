class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c) -> None:
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, value):
        if self.__check_value(value):
            self.__a = value
        
    @property
    def b(self):
        return self.__b
    
    @b.setter
    def b(self, value):
        if self.__check_value(value):
            self.__b = value
        
    @property
    def c(self):
        return self.__c
    
    @c.setter
    def c(self, value):
        if self.__check_value(value):
            self.__c = value
        
    @classmethod
    def __check_value(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION
    
    def __setattr__(self, __name: str, __value) -> None:
        if __name == 'MIN_DIMENSION' or __name == 'MAX_DIMENSION':
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        super().__setattr__(__name, __value)
        
        
d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30

d.MAX_DIMENSION = 10  # исключение AttributeError