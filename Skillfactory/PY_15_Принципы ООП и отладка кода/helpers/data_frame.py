import statistics

class DataFrame():
    def __init__(self, column, fill_value=0):
        #Инициализируем атрибуты
        self.column = column
        self.fill_value = fill_value
        #Заполним пропуски
        self.fill_missed()
        #Конвертируем все элементы в числа
        self.to_float()
        
    def fill_missed(self):
        for i, value in enumerate(self.column):
            if value is None or value == '':
                self.column[i] = self.fill_value
                
    def to_float(self):
        self.column = [float(value) for value in self.column]
        
    def median(self):
        return round(statistics.median(self.column), 2)
    
    def mean(self):
        return round(statistics.mean(self.column), 2)
    
    def deviation(self):
        return round(statistics.stdev(self.column), 2)