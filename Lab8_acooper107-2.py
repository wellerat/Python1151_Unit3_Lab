"""Geometry Calculator"""
"""Ann Cooper"""
"""Calulates the area and perimeter/circumference of circles and rectangles"""
"""No started code"""
"""Sept. 17, 2026"""

import circle as c
import rectangle as r
                    
run_program = True

while run_program:

    result_message=""

    print("\nGeometry Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumfrance")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")
 
    choice = input("\nEnter your choice (1-5)  ")

    if choice == '1':
        radius = (input("\nEnter radius of circle:  "))
        area = c.calc_area(float(radius))
        result_message=f"\nThe area of the circle is {area}"

    elif choice == '2':
        radius = (input("\nEnter radius of the circle:  "))
        circumference = c.calc_circumference(float(radius))
        result_message=f"\nThe circumference of the circle is {circumference}"

    elif choice == '3':
        width = (input("\nEnter width of rectangle:  "))
        height = (input("\nEnter height of rectangle: "))
        area = r.calc_area(float(width),float(height))
        result_message=f"\nThe area of the rectangle is {area}"

    elif choice == '4':
        width = (input("\nEnter width of rectangle:  "))
        height = (input("\nEnter height of rectangle: "))
        perimeter = r.calc_perimeter(float(width),float(height))
        result_message=f"\nThe perimeter of the rectangle is {perimeter}"

    elif choice == '5':
        print("\nGoodbye!")
        run_program=False
    
    else:
        print("\nInvalid entry, please try again....") 

    if result_message:
        print(result_message)
        input(f"\nPrint Enter to continue...")    

    



