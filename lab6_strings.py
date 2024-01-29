# Author : Andrea Laserna
# Created on November 11, 2022
# Modified on January 29, 2024

'''
Using two strings taken from a user input, write a function that returns True if the first string can be 
found inside the second string regardless of position. This should ignore upper/lower case differences 
(in other words, should not be “case sensitive”).
'''

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    print(string_search(string1, string2))

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == "y":
        main()
    elif choice.lower() == "n":
        print("Thank you for using this program!")
    else:
        print("Invalid input. Please try again.")

def string_search(string1, string2):
    if string1.lower() in string2.lower():
        return True
    else:
        return False

main()
