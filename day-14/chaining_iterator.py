#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

data = [1, 2, 3, 4, 5, 6]

result = reduce(
    lambda acc, x: acc + x,
    (x ** 2 for x in data if x % 2 == 0))

print(result) 
