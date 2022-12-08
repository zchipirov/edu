class Desc:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class MaxPooling:
    step = Desc()
    size = Desc()
    
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size
        
    def __call__(self, matrix, *args: any, **kwds: any) -> any:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        r = all([type(y) in (int, float) and len(x) == len(matrix) for x in matrix for y in x])
        if not r:
            raise ValueError("Неверный формат для первого параметра matrix.")
        
        h, w = self.size[0], self.size[1]
        sh, sw = self.step[0], self.step[1]
        
        rows_r = (rows - h) // sh + 1
        cols_r = (cols - w) // sw + 1
        
        res = [[0]*cols_r for _ in range(rows_r)]
        
        for i in range(rows_r):
            for j in range(cols_r):
                s = (x for r in matrix[i*sh: i* sh +h] for x in r[j*sw: j*sw+w])
                res[i][j] = max(s)
                
        return res
        

mp = MaxPooling()
r = mp([
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 8, 7, 6], 
    [5, 4, 3, 2]
    ])

print(r)