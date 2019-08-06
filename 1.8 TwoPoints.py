import math
# get the x coordinate of Point 1
x1 = int(input())  
# get the y coordinate of Point 2
y1 = int(input())  
# get the x coordinate of Point 2
x2 = int(input())
# get the y coordinate of Point 2
y2 = int(input())

# Write the code to calculate distance between 
# the two points 
value=(x2-x1)**2 + (y2-y1)**2
distance = math.sqrt(value)
print(distance)
