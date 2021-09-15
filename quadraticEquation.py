# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:56:19 2021
@author: Richard Paglia

Quadratic Equation
"""
# I had a lot of problem trying to get complex roots to show
# I was able to get it to work by researching online and using cmath over numpy

import cmath
import numpy as np

# Enter the 3 required variables a, b, c
# Error controlled to confirm a valid integer is entered
while True:
    try:
        aVariable = int(input("Enter the integer A variable: "))
        break
    except ValueError:
        print("\033[0;31;mNo valid integer! Please try again ...\033[0;0;m")

while True:
    try:
        bVariable = int(input("Enter the integer B variable: "))
        break
    except ValueError:
        print("\033[0;31;mNo valid integer! Please try again ...\033[0;0;m")

while True:
    try:
        cVariable = int(input("Enter the integer C variable: "))
        break
    except ValueError:
        print("\033[0;31;mNo valid integer! Please try again ...\033[0;0;m")


# Calculate the discriminant *needed to separate to calculate properly
discriminant = (bVariable**2) - (4 * aVariable * cVariable)

# Determine if a quadratic equation by making sure a != 0
if aVariable != 0:
    
    # if discriminant is greater than 0, calculate real root
    if discriminant > 0:
        posSolution = (-bVariable +np.sqrt(discriminant))/(2 * aVariable)
        negSolution = (-bVariable -np.sqrt(discriminant))/(2 * aVariable)
        print("{x+ = ", posSolution, "} and {x- = ", negSolution, "}")
        print("\n\033[0;36;mThis is a real root\033[0;0;m")
    
    # if discriminant is =0 calculate equal root    
    elif discriminant == 0:
        equalSolution = -bVariable/(2 * aVariable)
        print("{x = ", equalSolution, "}")
        print("\n\033[0;36;mThis is an equal root\033[0;0;m")
        
    # if discriminant is 'less than 0' (good movie!), calculate complex root
    elif discriminant < 0:
        posSolution = (-bVariable +cmath.sqrt(discriminant))/(2 * aVariable)
        negSolution = (-bVariable -cmath.sqrt(discriminant))/(2 * aVariable)
        print("{x+ = ", posSolution,"} and {x- = ", negSolution, "}")
        print("\n\033[0;36;mThis is a complex root\033[0;0;m")

else:
    # if a =0 this would not be a quadratic equation
    print("\n\033[0;31;mNot a quadratic equation\033[0;0;m")
