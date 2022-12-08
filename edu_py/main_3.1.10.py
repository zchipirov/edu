from doctest import FAIL_FAST
import time

class Mechanical:
    def __init__(self, date: float) -> None:
        self.__date = date
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, value):
        return True
    

class Aragon:
    def __init__(self, date: float) -> None:
        self.__date = date
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, value):
        return True
    
class Calcium:
    def __init__(self, date: float) -> None:
        self.__date = date
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, value):
        return True
    
class GeyserClassic:
    MAX_DATE_FILTER = 100
    slots = {'slot_1': None, 'slot_2': None, 'slot_3': None}
    
    def __init__(self) -> None:
        pass

    def add_filter(self, slot_num, filter):
        if type(filter) == Mechanical and slot_num == 1:
            if self.slots['slot_1'] is None:
                self.slots['slot_1'] = filter
        if type(filter) == Aragon and slot_num == 2:
            if self.slots['slot_2'] is None:
                self.slots['slot_2'] = filter
        if type(filter) == Calcium and slot_num == 3:
            if self.slots['slot_3'] is None:
                self.slots['slot_3'] = filter 
                
    def remove_filter(self, slot_num):
        self.slots[f'slot_{slot_num}'] = None    
        
    def get_filters(self):
        return (self.slots['slot_1'], self.slots['slot_2'], self.slots['slot_3'])   
    
    def water_on(self):
        if self.slots['slot_1'] is not None and self.slots['slot_2'] is not None and self.slots['slot_3'] is not None:
            if 0 <= time.time() - self.slots['slot_1'].date <= self.MAX_DATE_FILTER:
                return True
        return False
           
        
my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print('W=',w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print('W=',w)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
#print(f1.date)
print(f1,f2,f3)
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
