class Model:
    def __init__(self) -> None:
        self.__models = "Model"
        
    def query(self, **kwargs):
        self.__models += ": "+", ".join(map(lambda x: f"{x[0]} = {x[1]}", kwargs.items()))
        
    def __str__(self):
        return self.__models
        

model = Model()
model.query(id = 1, fio='Sergey', old=33)
print(model)