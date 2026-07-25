import math

x1 = int(input("ENTER THE COORDINATE X1 :")) 
x2 = int(input("ENTER THE COORDINATE X2 :"))
y1 = int(input("ENTER THE COORDINATE Y1 :"))
y2 = int(input("ENTER THE COORDINATE Y2 :"))

slope = (y2-y1)/(x2-x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"THE SLOPE : {slope}")
print(f"The straight line distance is: {int(distance)}")