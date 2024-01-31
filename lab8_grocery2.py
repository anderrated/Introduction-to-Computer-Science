# Author : Andrea Laserna
# Created on December 13, 2022
# Modified on January 31, 2024

'''
The mother loves the Grocery List program you created last time. Now she wants to make little 
adjustments to make it better. She wants to make sure that you list down the item’s prices and quantities 
as well.

Starting with just an empty dictionary, write a function that creates a grocery list that does the 
following:
• Add An Item (takes three inputs from the user: the name of the item, price for one item, and the 
quantity, then add it to the existing list)
• Remove An Item (takes a string input from the user and removes all instances from the list)
• Print Entire List (prints out all the contents of the list)
• Calculate Cost (prints out the total cost of the items in the list)
• Exit (exit the program)
'''
def main():
    grocery_list = {}
    run = True
    print("    GROCERY LIST    ")

    while run:
        print("====================\n")
        print("What would you like to do?")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Print entire list")
        print("4. Calculate cost")
        print("5. Exit\n")

        choice = input("Choice (1-4): ")
        try:
            int(choice)
        except ValueError:
            print("You can only choose from 1-4. Please try again.")
            continue
        
        print("====================")

        if choice == "1":
            add_item(grocery_list)
        elif choice == "2":
            remove_item(grocery_list)
        elif choice == "3":
            print_list(grocery_list)
        elif choice == "4":
            calculate(grocery_list)
        elif choice == "5":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid input. Please try again.")

def ask_price():
    while True:
        try:
            price = float(input("Price: "))
            break
        except:
            print("Price must be a number. Try Again\n")
    return price

def ask_quantity():
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except:
            print("Quantity must be a number. Try Again\n")
    return quantity

def add_item(grocery_list):
    print("ADD AN ITEM...")

    item_to_add = input("Name: ")

    for item, (price, quantity) in list(grocery_list.items()):
        if item_to_add.lower() == item.lower():
            print("Item already exists. Try Again\n")
            add_item(grocery_list)
            return

    price = ask_price()
    quantity = ask_quantity()

    grocery_list[item_to_add] = (price, quantity)

    

def remove_item(grocery_list):
    print("REMOVE AN ITEM...")

    item_to_remove = input("Enter the item to remove: ")
    for item, (price, quantity) in list(grocery_list.items()):
        if item_to_remove.lower() == item.lower():
            grocery_list.pop(item)
            return
        else:
            print("Item not found.\n")

def print_list(grocery_list):
    print("PRINTING LIST...\n")
    print(f'{"ITEM": <11} {"PRICE": <11} {"QUANTITY"}\n')

    for item, (price, quantity) in grocery_list.items():
        print(f"{item: <12} {price: <12} {quantity}")

def calculate(grocery_list):
    print("CALCULATING COST...\n")
    total = 0
    print_list(grocery_list)

    for item, (price, quantity) in grocery_list.items():
        total += price * quantity

    print(f"\nTotal cost: ${total}")

main()