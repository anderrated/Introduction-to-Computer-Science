# Author : Andrea Laserna
# Created on October 1, 2022
# Modified on January 29, 2024

'''
EXERCISE # 1 - Giving A Description

Write a function that determines some characteristics of a certain integer n whose value is taken 
from a user input. These characteristics include:
• If n is odd or even
• If n is positive, negative, or neither
• If n is divisible by 3
• If the absolute value of n is between 50 and 99 inclusive
'''

n = int(input("Enter a number 'n': "))
print("=== A SHORT DESCRIPTION OF '" + str(n) + "' ===")

# Odd or Even

if (n % 2 == 0):
    print("'" + str(n) + "' is EVEN.")
else:
    print("'" + str(n) + "' is ODD.")

# Positive, Negative, Neither

if (n > 0):
    print("'" + str(n) + "' is POSITIVE.")
elif (n < 0):
    print("'" + str(n) + "' is NEGATIVE.")
else:
    print("'" + str(n) + "' is NEITHER POSITIVE NOR NEGATIVE.")

# Divisible by 3

if (n == 0):
    print("'" + str(n) + "' is NOT DIVISIBLE BY 3.")
elif (n % 3 == 0):
    print("'" + str(n) + "' is DIVISIBLE BY 3.")
else:
    print("'" + str(n) + "' is NOT DIVISIBLE BY 3.")

# Absolute Value

if (abs(n) >= 50 and abs(n) <= 99):
    print("'" + str(n) + "' is IN BETWEEN 50 AND 99 INCLUSIVE.")
else:
    print("'" + str(n) + "' is NOT IN BETWEEN 50 AND 99 INCLUSIVE.")

