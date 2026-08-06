#Creating DataFrames from List of Lists
import pandas as pd
data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

#Creating DataFrame Using Dictionary
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

#Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

#Reading CSV File Using Pandas
#before implementing .csv file open the respective directory in the terminal in order to perform any operation on it
df = pd.read_csv('employees.csv')
print(df)

print(df.head())  #read only first five rows of the employees data
print(df.tail())  #read only last five rows of the employees data
print(df.shape)   #OUTPUT: (1000,8) [(rows,columns)]
print(df.columns)  #return column name
teams = print(['Team'])
print(teams)  #print the data in column 'Team'
