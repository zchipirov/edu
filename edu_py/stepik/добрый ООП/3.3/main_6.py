import math


class Complex:
    @staticmethod
    def __check_type(value):
        if type(value) not in [float, int]:
            raise ValueError("Неверный тип данных.")
    
    @property
    def real(self):
        return self.__real
    
    @real.setter
    def real(self, value):
        self.__check_type(value)
        self.__real = value
        
    @property
    def img(self):
        return self.__img
    
    @img.setter
    def img(self, value):
        self.__check_type(value)
        self.__img = value
        
    def __init__(self, real, img) -> None:
        self.real = real
        self.img = img
        
    def __abs__(self):
        return math.sqrt(self.real**2 + self.img**2)
        
cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)