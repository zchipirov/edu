class ListMath:
    def __init__(self, lst = None) -> None:
        self.lst_math = [x for x in lst if type(x) in (int, float)] if lst and type(lst) == list else []
    
    @staticmethod
    def __raise_type_error(other):
        if type(other) not in (int, float):
            raise ArithmeticError("Неправильный аргумент")
    
    def __add__(self, other):
        self.__raise_type_error(other)
        
        return ListMath(list(map(lambda x: x + other, self.lst_math)))

    def __radd__(self, other):
        self.__raise_type_error(other)
        
        return ListMath(list(map(lambda x: x + other, self.lst_math)))
    
    def __iadd__(self, other):
        self.__raise_type_error(other)
        
        self.lst_math = list(map(lambda x: x + other, self.lst_math))
        
        return self
    
    def __sub__(self, other):
        self.__raise_type_error(other)
        
        return ListMath(list(map(lambda x: x - other, self.lst_math)))
    
    def __rsub__(self, other):
        self.__raise_type_error(other)
        
        return ListMath(list(map(lambda x: other - x, self.lst_math)))
    
    def __isub__(self, other):
        self.__raise_type_error(other)
        
        self.lst_math = list(map(lambda x: x - other, self.lst_math))
        
        return self
    
    def __mul__(self, other):
        self.__raise_type_error(other)
        
        return ListMath(list(map(lambda x: x * other, self.lst_math)))
    
    def __rmul__(self, other):
        self.__raise_type_error(other)
        
        return ListMath(list(map(lambda x: x * other, self.lst_math)))
    
    def __imul__(self, other):
        self.__raise_type_error(other)
        
        self.lst_math = list(map(lambda x: x * other, self.lst_math))
        
        return self
    
    def __truediv__(self, other):
        self.__raise_type_error(other)
        
        return ListMath(list(map(lambda x: x / other, self.lst_math)))
    
    def __rtruediv__(self, other):
        self.__raise_type_error(other)
        
        return ListMath(list(map(lambda x: other / x, self.lst_math)))
    
    def __itruediv__(self, other):
        self.__raise_type_error(other)
        
        self.lst_math = list(map(lambda x: x / other, self.lst_math))
        
        return self

lst = ListMath([1, "abc", -5, 7.68, True])
print(lst.__dict__)
lst = lst - 76 # вычитание из каждого числа списка определенного числа
print(lst.__dict__)
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
