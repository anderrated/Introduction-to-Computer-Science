# Author : Andrea Laserna
# Created on October 1, 2022
# Modified on January 29, 2024

'''
EXERCISE # 2 - The X Factorial

Write a function that solves for the factorial of an integer n. The factorial of a number is a sequential 
multiplication operation of all the natural numbers that are less than it. 
'''

n = int(input("Enter a number 'n': "))

# Base cases
if (n == 0 or n == 1):
    print(f"The factorial of {n} is 1")
else:
# Recursive case
    print(f"The factorial of {n} is {n} * {n-1} = {n * (n-1)}")