#names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 
#Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

nordic_countries = names[:5]
es = names[5]
ru = names[6]   

print(nordic_countries)    #OUTPUT: ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print(es)    #OUTPUT: Estonia
print(ru)    #OUTPUT: Russia
