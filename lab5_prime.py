# Author : Andrea Laserna
# Created on October 30, 2022
# Modified on January 29, 2024

'''
Write a function that determines the first n prime numbers. The value of n is taken from a user input. 
The program should print all the prime numbers requested.
'''
import math

def prime(n):
    count = 0
    num = 2
    while count < n:
        prime = True

        # If the number is not divisible by any number between 2 and the number before itself, it is a prime number
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if (prime):     
            count += 1     
            print(num)

        num += 1
             
def main():
    choice = "y"
    n = int(input("Enter the value of n: "))
    print(f"=== The first {n} PRIME NUMBERS ===")
    prime(n)

    choice = input("Do you want to continue? (y/n) \n")
    if choice.lower() == "y":
        main()
    elif choice.lower() == "n":
        print("Thank you for using this program!")
    else:
        print("Invalid input. Please try again.")

main()