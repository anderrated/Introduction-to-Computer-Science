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

# EXERCISE 2

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