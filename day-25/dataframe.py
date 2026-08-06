#Creating a DataFrame
import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

weights = [74, 78, 69]
df['Weight'] = weights
df    #added a new column

heights = [173, 175, 169]
df['Height'] = heights
print(df)

df['Height'] = df['Height'] * 0.01
df    #modifying the columns

#calculating the bmi
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
bmi = calculate_bmi()

df['BMI'] = bmi
df

df['BMI'] = round(df['BMI'], 1) #rounded off to one digit after the decimal point
print(df)

print(df.Weight.dtype) #returns the datatype OTPUT: int64
