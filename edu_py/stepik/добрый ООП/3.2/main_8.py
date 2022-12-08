class Handler:
    def __init__(self, methods=('GET', )):
        self.__methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
           m = request.get('method', 'GET') 
           if m in self.__methods:
               method = m.lower()
               return self.__getattribute__(method)(func, request)
        
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'
    
    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'


@Handler
def contact(request):
    return "Cthdasd"

print(type(contact))
a = contact({'method': 'GET', 'url': 'contact.html'})
print(a)