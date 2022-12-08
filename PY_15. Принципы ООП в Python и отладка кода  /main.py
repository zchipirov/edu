class DepartmentReport:
    def __init__(self) -> None:
        self.revenues = []
        
    def add_revenue(self, amount):
        """
        Метод для добавления выручки отдела в список revenues.
        Если атрибута revenues ещё не существует, метод должен создавать пустой список перед добавлением выручки.
        """
        self.revenues.append(amount)
    
    def average_revenue(self):
        """
        Метод возвращает среднюю выручку по отделам.
        """
        return round(sum(self.revenues)/len(self.revenues), 1)
    

report = DepartmentReport()
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.revenues)
# => [1000000, 400000]
print(report.average_revenue())
# => 700000.0
      