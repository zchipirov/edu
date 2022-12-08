class Name:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Money:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if type(value) in (int, float):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class ItemsList:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
         
    
class Budget:
    items_list = ItemsList()
    
    def __init__(self) -> None:
        self.items_list = []
    
    def add_item(self, it):
        self.items_list.append(it)
    
    def remove_item(self, indx):
        del self.items_list[indx]
    
    def get_items(self):
        return [x for x in self.items_list]


class Item:
    name = Name()
    money = Money()
    
    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money
        
    def __add__(self, other):
        return self.money + other
    
    def __radd__(self, other):
        return self.__add__(other)
        
        
my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
    
print(s)
