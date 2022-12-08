class HandlerGET:
    def __init__(self, func):
        self.__func = func

    def __call__(self, request, *args, **kwargs):
        m = request.get('method', 'GET')
        if m == 'GET':
            return self.get(self.__func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'


@HandlerGET
def contact(request):
    return "Cthdasd"

print(type(contact))
a = contact({'method': 'GET', 'url': 'contact.html'})
print(a)