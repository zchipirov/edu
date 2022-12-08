class InputDigits:
    def __init__(self, func) -> None:
        self.__func = func
    
    def __call__(self, *args: any, **kwds: any) -> any:
        return list(map(int, self.__func().split()))
    
def input_dg():
    x = input()
input_dg = InputDigits(input)
res = input_dg()
print(res)