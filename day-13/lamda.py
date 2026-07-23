#Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, x2, y1, y2: (y2 - y1)/(x2-x1)
print(slope(5,3,4,2))

y_intercept = lambda x1, x2, y1, y2 : y1 - slope (x1,x2,y1,y2) * x1
print(y_intercept(5,3,4,2))
