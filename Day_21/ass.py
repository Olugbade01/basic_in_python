import statistics
class StatisticOperator:
    def __init__(self,listed_items):
        self.listed_items = listed_items

    def count(self):
        couunts = len(self.listed_items)
        return couunts
    def sum(self):
        total = 0
        for age in self.listed_items:
            total += age
        return total

    def min(self):
        return min(self.listed_items)
    def max(self):
        maxi = max(self.listed_items)
        return maxi
    def range(self):
        range_ = max(self.listed_items) - min(self.listed_items)
        return range_

    def mean(self):
        datas = self.listed_items
        mean_val = statistics.mean(datas)
        return mean_val
    def median(self):
        datas = self.listed_items
        median_val = statistics.median(datas)
        return median_val
    def mode(self):
        datas = self.listed_items
        mode_counts = 0
        mode_val =  statistics.mode(datas)
        for element in datas:
            if element == mode_val:
                mode_counts += 1
        return {'mode': mode_val, 'counts': mode_counts}
    def std(self):
        datas = self.listed_items
        std_dev = statistics.stdev(datas)
        return round(std_dev, 2)
    def var(self):
        datas = self.listed_items
        variance = statistics.variance(datas)
    
        return round(variance, 2)

    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = StatisticOperator(ages)

print(data.count())
print(data.sum())
print(data.min())
print(data.range())
print(data.mean())
print(data.median())
print(data.mode())
print(data.std())
print(data.var())