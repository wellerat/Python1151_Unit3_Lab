"""
Circle Geometry Calculator

Description:
   Calculates the area and circumference of circles.
   
Author:   
   Ann Cooper

Starter Code: 
   No starter code
   
Date:
   Sept. 17, 2026
"""

import math

def calc_area(radius):
    """Calculate the area of a circle"""
    circle_area = math.pi * (radius ** 2)
    return circle_area


def calc_circumference(radius):
    """Calculate the circumference of a circle"""
    circle_circumference = 2*radius*math.pi
    return circle_circumference