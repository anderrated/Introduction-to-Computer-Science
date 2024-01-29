# Author : Andrea Laserna
# Created on October 20, 2022
# Modified on January 29, 2024

'''
Write a set of functions that help determine the type of a triangle based on its angles whose values
are taken from user input.
'''
def main():
    angle1 = int(input("Enter the first angle: "))
    angle2 = int(input("Enter the second angle: "))
    angle3 = int(input("Enter the third angle: "))
    
    print(triangle_type(angle1, angle2, angle3))

def angle_type(angle):
    if (angle > 0  and angle < 90):
        return "acute"
    elif (angle == 90):
        return "right"
    elif (angle > 90 and angle < 180):
        return "obtuse"
    else:
        return "invalid"

def is_triangle(angle1, angle2, angle3):
    if (angle1 + angle2 + angle3 == 180):
        return True
    else:
        return False

def triangle_type(angle1, angle2, angle3):
    if is_triangle(angle1, angle2, angle3):
        if (angle_type(angle1) == "right" or angle_type(angle2) == "right" or angle_type(angle3) == "right"):
            return "The three angles form a RIGHT triangle"
        elif (angle_type(angle1) == "acute" and angle_type(angle2) == "acute" and angle_type(angle3) == "acute"):
            return "The three angles form an ACUTE triangle"
        elif (angle_type(angle1) == "obtuse" or angle_type(angle2) == "obtuse" or angle_type(angle3) == "obtuse"):
            return "The three angles form an OBTUSE triangle"
    else:
        return "The three angles DO NOT form a triangle."

main()