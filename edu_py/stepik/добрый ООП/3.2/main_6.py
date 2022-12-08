class RenderList:
    lst = []
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ("ul", "ol") else "ul"
    
    def __call__(self, *args: any, **kwds: any) -> any:
        return '\n'.join([f'<{self.type_list}>', *map(lambda x: f'<li>{x}</li>', args[0]), f'</{self.type_list}>'])
       
        
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ul")
html = render(lst)
print(html)