
dog = {}


dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 3

print("Dog Dictionary:")
print(dog)

student = {
    "first_name": "Pratham",
    "last_name": "Pai",
    "gender": "Male",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "HTML"],
    "country": "India",
    "city": "Mangalore",
    "address": "Karnataka"
}

print("\nStudent Dictionary:")
print(student)

print("\nLength of Student Dictionary:")
print(len(student))



# 5. Get the value of skills and check the data type
print("\nSkills:")
print(student["skills"])

print("Data Type of Skills:")
print(type(student["skills"]))



student["skills"].append("CSS")
student["skills"].append("JavaScript")

print("\nUpdated Skills:")
print(student["skills"])



# 7. Get the dictionary keys as a list
print("\nDictionary Keys:")
print(list(student.keys()))

print("\nDictionary Values:")
print(list(student.values()))



print("\nDictionary as List of Tuples:")
print(list(student.items()))




del student["address"]

print("\nStudent Dictionary after deleting 'address':")
print(student)


del dog

print("\nDog dictionary deleted successfully.")