class Stack:
    def __init__(self) -> None:
        self.top = self.__last = None
    
    def push_back(self, obj):
        if self.top is None:
            self.top = self.__last = obj
        else:
            self.__last.next = obj
            self.__last = obj
    
    def pop_back(self):
        if self.top.next:
            temp = self.top
            while temp.next.next:
                temp = temp.next
            temp.next = None
        else:
            self.top = None
    
    def show(self):
        so = self.top
        if so is None:
            return None
        while so:
            print(so.data, end=' ')
            so = so.next

    def __add__(self, other):
        if not isinstance(other, StackObj):
            raise TypeError('Неверный тип данных')
        
        self.push_back(other)
        return self
    
    def __iadd__(self, other):
        if not isinstance(other, StackObj):
            raise TypeError('Неверный тип данных')
        
        self.push_back(other)
        return self
    
    def __mul__(self, other):
        if not isinstance(other, list):
            raise TypeError('Неверный тип данных')
        
        for x in other:
            self.push_back(StackObj(x))
        return self
    
    def __imul__(self, other):
        if not isinstance(other, list):
            raise TypeError('Неверный тип данных')
        
        for x in other:
            self.push_back(StackObj(x))
        return self
        

class StackObj:
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, value):
        self.__next = value
        
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None
        
        
h = StackObj('5')
print(h._StackObj__data) # 5
st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
st.show() # 1 2 3
st = st + StackObj('4')
print()
st.show()
st += StackObj('5')
print()
st.show()
st = st * [str(i) for i in range(6, 9)]
print()
st.show() # 1 2 3 4 5 6 7 8 9 10 11 12
st *= [str(i) for i in range(9, 12)]
print()
st.show() # 1 2 3 4 5 6 7 8 9 10 11 12
print()
print([str(i) for i in range(6, 9)])