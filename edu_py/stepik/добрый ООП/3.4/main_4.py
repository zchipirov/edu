class NewList:
    def __init__(self, lst = None) -> None:
        self._lst = lst[:] if lst and type(lst) == list else []
    
    def get_list(self):
        return self._lst
        
    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("Неверный тип данных")
        
        other_list = other
        if isinstance(other, NewList):
            other_list = other._lst
            
        return NewList(self.__diff_list(self._lst, other_list))
    
    @staticmethod
    def __diff_list(l1, l2):
        if len(l2) == 0:
            return l1
        
        sub = l2[:]
        return [x for x in l1 if not NewList.__is_elem(x, sub)]
    
    @staticmethod
    def __is_elem(el, l):
        res = any(map(lambda x: type(el) == type(x) and x == el, l))
        if res:
            l.remove(el)
        return res
                
    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError("Неверный тип данных")
        
        return NewList(self.__diff_list(other, self._lst))


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.__dict__)
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.__dict__)

print(lst2.__dict__)
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
print(res_2.__dict__)
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
print(res_3.__dict__)
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4.__dict__)