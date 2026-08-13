import math
# Ask user to input coordinates
x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))

# Calculate the distance between the two points
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Print the distance            
print("The distance between the two points is:", distance)

#REFLECTION:
# Using the math library in the program makes things simpler because it provides built-in functions like sqrt() and pow(). 
# Without these functions, it would take more time and it would be more difficult to write correctly.
