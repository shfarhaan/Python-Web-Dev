# Homework:
# 1.Write a function to Calculate the area of a circle with given radius


"""

This function takes the radius of a circle as input and returns its area. 
The formula for the area of a circle is *πr²*.

"""

import math

def calculate_circle_area(radius):
    """
        Calculates the area of a circle with a given radius.
    """
    if radius < 0:
        return "Error: Radius cannot be negative."
    return math.pi * (radius ** 2)

radius1 = 5
area1 = calculate_circle_area(radius1)
print(f"The area of a circle with radius {radius1} is: {area1}")

radius2 = 10
area2 = calculate_circle_area(radius2)
print(f"The area of a circle with radius {radius2} is: {area2}")


