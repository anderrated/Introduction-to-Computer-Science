# Author: Andrea Laserna
# Date of Creation: 2022
# This laboratory exercise will utilize the math module
import math

# EXERCISE 1 - The Python Math Module

w = 0
x = 14
y = -8
z = 32

num1 = x * z - math.pow(x, 2) 
print(num1)

num2 = x / (y + z)
print(num2)

num3 = math.sqrt(z + x * w)
print(num3)

num4 = math.tan(y)
print(num4)

num5 = math.log10(x)
print(num5)

num6 = 9 * math.pow(10, -7)
print(num6)

# EXERCISE 2 - Boolean Expressions

myGWA = 1.69
laude = 1.75
magna = 1.45
summa = 1.2

print(myGWA < magna)
print(myGWA > 1.69)
print(myGWA == laude)
print((myGWA >= laude) and (myGWA < summa))
print((myGWA > magna) or (myGWA <= laude))
print(5 * 0.15 == 0.75)

# EXERICSE 3 - Strings and Basic Printing

chocolate = 12
strawberry = 5
vanilla = 20

print(chocolate, strawberry, vanilla)
print(str(chocolate) + " and " + str(vanilla))
print("There are " + str(chocolate) + " chocolate, " + str(strawberry) + " strawberry and " + str(vanilla) + " vanilla ice cream.")
print("The total number of ice cream is", chocolate + strawberry + vanilla)

# EXERCISE 4 - Math expressions

width = 24
height = 11.0
delimiter = "."

no1 = width / 3
print(no1)

no2 = width / 3.0
print(no2)

no3 = height * 3
print(no3)

no4 = 1 + 4 * 3
print(no4)

no5 = delimiter *6 
print(no5)

# EXERCISE 5

'''
The volume of a cone with radius r and height h is 1/3πr^2
h. What is the volume of a cone with 
radius 7 and height 13?
'''

r = 7
h = 13
volume = 1 / 3 * math.pi * math.pow(r, 2)
print("The volume is " + str("%.2f" % volume))

'''
Suppose the cover price of Taylor Swift’s new and exclusive “Folklore” album is $11.99, but
digital stores get a 30% discount. Shipping costs $4 for the first copy and 85 cents for each 
additional copy. What is the total wholesale cost for 125 copies?
'''
price = 11.99
discount = 0.3
shipping_cost = 4
additional_copy = 0.85
copies = 125

total_cost = copies * (price - (price *discount)) + shipping_cost + (additional_copy * 124)
print("The total cost is " + str("%.2f" % total_cost))
