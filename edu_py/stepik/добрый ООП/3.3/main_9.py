class Ingredient:
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, value):
        self.__volume = value
        
    @property
    def measure(self):
        return self.__measure
    
    @measure.setter
    def measure(self, value):
        self.__measure = value
    
    def __init__(self, name, volume, measure) -> None:
        self.__name = name
        self.__volume = volume
        self.__measure = measure
    
    def __str__(self) -> str:
        return f"{self.__name}: {self.__volume}, {self.__measure}"


class Recipe:
    @property
    def ing_lst(self):
        return self.__ing_lst
    
    @ing_lst.setter
    def ing_lst(self, value):
        self.__ing_lst = value
        
    def __init__(self, *args) -> None:
        self.ing_lst = []
        for ing in args:
            if isinstance(ing, Ingredient):
                self.ing_lst.append(ing)
    
    def add_ingredient(self, ing):
        if isinstance(ing, Ingredient):
            self.ing_lst.append(ing)
    
    def remove_ingredient(self, ing):
        self.ing_lst.remove(ing)
    
    def get_ingredients(self):
        #return tuple(map(lambda x: str(x), self.ing_lst))
        return tuple(map(lambda x: x, self.ing_lst))
    
    def __len__(self):
        return len(self.ing_lst)
    

recipe = Recipe()
recipe.add_ingredient("asd")
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))

print(recipe)
ings = recipe.get_ingredients()
print(ings)
n = len(recipe) # n = 3
print(n)