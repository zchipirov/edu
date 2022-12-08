class PolyLine:
    @property
    def lines(self):
        return self.__lines
    
    @lines.setter
    def lines(self, value):
        self.__lines = value
        
    def __init__(self, start_coord = (), *args) -> None:
        self.lines = []
        self.lines.append(start_coord)
        for i in args:
            self.lines.append(i)
    
    def add_coord(self, x, y):
        self.lines.append((x, y))
    
    def remove_coord(self, indx):
        del self.lines[indx]
    
    def get_coords(self):
        return self.lines