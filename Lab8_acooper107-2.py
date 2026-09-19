"""Geometry Calculator"""
"""Ann Cooper"""
"""Calulates the area and perimeter/circumference of circles and rectangles"""
"""No started code"""
"""Sept. 17, 2026"""


                    
run_program = True

while run_program:
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
    elif choice == '2':
        radius = (input("\nEnter radius of the circle:  "))
    elif choice == '3':
        width = (input("\nEnter width of rectangle:  "))
        height = (input("\nEnter height of rectangle: "))
    elif choice == '4':
        width = (input("\nEnter width of rectangle:  "))
        height = (input("\nEnter height of rectangle: "))
    elif choice == '5':
        print("\nGoodbye!")
        run_program=False 

    else:
        print("\nInvalid entry, please try again....")     



