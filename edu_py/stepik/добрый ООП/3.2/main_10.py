class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.__render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))
        return wrapper


class RenderDigit:
    def __call__(self, dig, *args: any, **kwds: any) -> any:
        if dig[0] == '-':
            if dig[1:].isdigit():
                return int(dig)
        elif dig.find('.') == -1 and dig.isdigit():
            return int(dig)
        return None

render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)