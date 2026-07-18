print("Who is older (me or you)?")

my_age = 20
your_age = int(input("Enter your age: "))

if your_age < my_age:
    difference = my_age - your_age

    if difference == 1:
        print(f"You are {difference} year younger than me.")
    else:
        print(f"You are {difference} years younger than me.")

elif your_age > my_age:
    difference = your_age - my_age

    if difference == 1:
        print(f"You are {difference} year older than me.")
    else:
        print(f"You are {difference} years older than me.")

else:
    print("We are the same age.")