import numpy as np

class DigitRetrieve:    
    def __call__(self, *args: any, **kwds: any) -> any:
        if args[0][0] == '-':
            if args[0][1:].isdigit():
                return int(args[0])
        elif args[0].find('.') == -1 and args[0].isdigit():
            return int(args[0])
        return None
        

dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)