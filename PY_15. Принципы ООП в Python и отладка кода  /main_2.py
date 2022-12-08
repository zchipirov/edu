class DepartmentReport:

    def __init__(self,company):
        """
        Метод инициализации класса. 
        Создаёт атрибуты revenues и company
        """
        self.revenues = []
        self.company = company
    
    def add_revenue(self, amount):
        """
        Метод для добавления выручки отдела в список revenues.
        Если атрибута revenues ещё не существует, метод должен создавать пустой список перед добавлением выручки.
        """
        self.revenues.append(amount)
    
    def average_revenue(self):
        """
        Вычисляет average_revenue — среднюю выручку по отделам — округляя до целого.
        Метод возвращает строку в формате:
        'Average department revenue for <company>: <average_revenue>'
        """
        average = round(sum(self.revenues)/len(self.revenues), 1)
        return f'Average department revenue for {self.company}: {int(average)}'
    
report = DepartmentReport("Danon")
report.add_revenue(1_000_000)
report.add_revenue(400_000)

print(report.average_revenue())
# => Average department revenue for Danon: 700000
      