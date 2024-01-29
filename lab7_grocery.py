# Author : Andrea Laserna
# Created on November 25, 2022
# Modified on January 29, 2024

'''
A mother wants to list down the things she needs to buy, however, she needs a simple list that be run 
every time and can be modified whenever she changes her mind.

Starting with just an empty list, write a function that creates a grocery list that does the following:
• Add an Item (takes a string input from the user and add it to the existing list)
• Remove an Item (takes a string input from the user and removes all instances from the list)
• Print entire list (prints out all the contents of the list)
• Exit (exit the program)
'''

def main():
    grocery_list = []
    run = True
    print("    GROCERY LIST    ")
    print("====================")

    while run:
        print("What would you like to do?")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Print entire list")
        print("4. Exit\n")
        choice = input("Choice (1-4): ")
        print("====================")

        if choice == "1":
            add_item(grocery_list)
        elif choice == "2":
            remove_item(grocery_list)
        elif choice == "3":
            print_list(grocery_list)
        elif choice == "4":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid input. Please try again.")

def add_item(grocery_list):
    item = input("Enter the item to add: ")
    grocery_list.append(item)
    print("====================\n")

def remove_item(grocery_list):
    item_to_remove = input("Enter the item to remove: ")
    for item in grocery_list:
        if item_to_remove.lower() == item.lower():
            grocery_list.remove(item)
        else:
            print("Item not found.")
    print("====================\n")

def print_list(grocery_list):
    print("PRINTING LIST...\n")
    for item in grocery_list:
        print(item)
    print("====================\n")

main()