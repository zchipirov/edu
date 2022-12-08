class Clock:
    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        self.__hours = value
    
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self, value):
        self.__minutes = value    
    
    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, value):
        self.__seconds = value  
          
    def __init__(self, hours, minutes, seconds) -> None:
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    
    def get_time(self):
        return self.__hours*3600 + self.minutes*60 + self.seconds
    
    @staticmethod
    def get_time_str(value):
        h = value / 3600
        m = (h - int(h))*60
        s = (m - int(m))*60
        return f"{int(h):02}: {int(m):02}: {round(s):02}"


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self.__clock1 = clock1
        self.__clock2 = clock2
    
    def __str__(self) -> str:
        return Clock.get_time_str(self.__delta_time(self.__clock1.get_time(), self.__clock2.get_time()))
    
    @staticmethod
    def __delta_time(clock1, clock2):
        delta = clock1 - clock2
        return [delta, 0][delta<0]
        
    def __len__(self):
        return self.__delta_time(self.__clock1.get_time(), self.__clock2.get_time())


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)
str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)