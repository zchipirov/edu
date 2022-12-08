class ObjList:
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
        
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, value):
        self.__prev = value
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, value):
        self.__next = value
        
    def __init__(self, data) -> None:
        self.data = data
        self.prev = self.next = None
    
    
class LinkedList:
    def __init__(self, head: ObjList = None, tail: ObjList = None) -> None:
        self.head = head
        self.tail = tail
    
    @property
    def head(self):
        return self.__head
    
    @head.setter
    def head(self, value):
        self.__head = value
        
    @property
    def tail(self):
        return self.__tail
    
    @tail.setter
    def tail(self, value):
        self.__tail = value
        
    def add_obj(self, obj: ObjList):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        
        if not self.head:
            self.head = obj
            
    def print_next(self):
        obj = self.head
        while obj is not None:
            print(obj.prev)
            obj = obj.next
            
        
    def remove_obj(self, indx):
        i = 0
        obj = self.head
        while obj is not None:
            if i == indx:
                # remove and exit
                #print(obj)
                prev = obj.prev
                next = obj.next
                if prev is not None:
                    prev.next = obj.next
                else:
                    self.head = next
                if next is not None:
                    next.prev = prev
                else:
                    self.tail = prev
            else:
                # next
                obj = obj.next
            i += 1

    def __len__(self):
        c = 0
        obj = self.head
        while obj is not None:
            obj = obj.next
            c += 1
        return c
    
    def __call__(self, indx, *args: any, **kwds: any) -> any:
        i = 0
        obj = self.head
        while obj is not None:
            if i == indx:
                # remove and exit
                return obj.data
            else:
                # next
                obj = obj.next
                i += 1
        return None
    

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(0)
#linked_lst.print_next()
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
print(n)
s = linked_lst(1) # s = Balakirev
print(s)
