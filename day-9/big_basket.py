fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print("Modified list:", fruits)