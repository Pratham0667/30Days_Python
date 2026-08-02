#Python has the module called statistics and we can use this module to do all the statistical calculations.
#However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
#In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. 
#You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. 
#Check the output below.
from statistics import mean, median, mode, stdev, variance
from collections import Counter

class Statistics:
    def __init__(self, data):
        if not data:
            raise ValueError("Data list cannot be empty.")
        self.data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(mean(self.data))

    def median(self):
        return median(self.data)

    def mode(self):
        try:
            mode_val = mode(self.data)
            count_val = self.data.count(mode_val)
            return (mode_val, count_val)
        except Exception:
            return (None, 0)

    def std(self):
        return round(stdev(self.data), 1)

    def var(self):
        return round(variance(self.data), 1)

    def freq_dist(self):
        total = self.count()
        counts = Counter(self.data)
        sorted_items = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
        return [(round((count / total) * 100, 1), value) for value, count in sorted_items]

    def describe(self):
        lines = [
            f"Count: {self.count()}",
            f"Sum:  {self.sum()}",
            f"Min:  {self.min()}",
            f"Max:  {self.max()}",
            f"Range: {self.range()}",
            f"Mean:  {self.mean()}",
            f"Median:  {self.median()}",
            f"Mode:  {self.mode()}",
            f"Variance:  {self.var()}",
            f"Standard Deviation:  {self.std()}",
            f"Frequency Distribution: {self.freq_dist()}"
        ]
        return "\n".join(lines)
      
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print(data.describe())
print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())   
