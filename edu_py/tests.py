import statistics 
class IntDataFrame:
    def __init__(self, lst):
        self.lst = list(map(int, lst))
        
    def count(self):
        return len(list(filter(lambda x: x>0, self.lst)))
    
    def unique(self):
        return len(set(self.lst))
    
df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.count())
# => 5
print(df.unique())
# => 4
