#pip install pandas  (for installation purposes)

#Creating Pandas Series with Default Index
import pandas as pd
import numpy as np

nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

#Creating Pandas Series with custom index
fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

#Creating Pandas Series from a Dictionary
dct = {'name':'Anvesha','country':'India','city':'Mangalore'}
s = pd.Series(dct)
print(s)

#Creating a Constant Pandas Series
s = pd.Series(10, index = [1, 2, 3])
print(s)

#Creating a Pandas Series Using Linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)
