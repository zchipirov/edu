class ImageFileAcceptor:
    def __init__(self, extensions):
        self.__extensions = extensions
        
    def __call__(self, *args, **kwargs):
        if len(args[0]) > 0 and args[0][args[0].find('.')+1:] in self.__extensions:
            return True
        return False
            
    
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]




