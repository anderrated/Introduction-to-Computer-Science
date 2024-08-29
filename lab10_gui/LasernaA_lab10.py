# Author: A. Laserna
# Date: 10/27/2020
# Description: This program is a grocery list UI

from UI import *

# Add an item to the grocery list
def additem(groceries):
    # write prompt to textbox
    write('ADD AN ITEM')
    # callback function for confirming entries
    def onConfirm():
        try:
            # get the values from the entry widgets
            itemvalue = item()
            quantityvalue = int(quantity())
            pricevalue = float(price())
            # check if the item already exists in the list
            if itemvalue.lower() in [x.lower() for x in groceries.keys()]:
                write("try again")
            else:
                # add the item to the list
                groceries[itemvalue]=(pricevalue,quantityvalue)
                # remove the entry widgets and call the prompt function
                removeEntryFrame()
                prompt()
        except:
            write("try again")
    #assigning returned values 
    (item,quantity,price) = createEntries(["Item Name", "Quantity", "Price"], onConfirm)

# Remove an item from the grocery list
def remove(groceries):
    write('REMOVE AN ITEM')
    def onConfirm():
        try:
            removeName = item()
            # remove the item if it exists
            dictName = [name for name in groceries.keys() if removeName == name.lower()][0]
            groceries.pop(dictName)
            removeEntryFrame()
            prompt()
        except:
            write("Item does not exist in groceries")
            removeEntryFrame()
            prompt()
    # get the item name from the entry widget
    [item] = createEntries(["Item Name"], onConfirm)

# Print the grocery list to the textbox
def printing(groceries):
    write ("PRINTING LIST...")
    write("\n")
    # loop through the items and write each one to a new line
    for (item,(price,quantity)) in groceries.items():
        write (f"{item:12s} {price:f} {quantity:6d}")
    prompt()

# Calculate and display the total cost of the groceries
def cost(groceries):
    cost=0
    # loop through the groceries and sum the price * quantity for total cost
    for (_,(price,quantity)) in groceries.items():
        cost+=price*quantity
    write("\n")
    write (f"TOTAL COST: {cost}")
    write ("="*21)
    prompt()

def prompt():
    write ("What would you like to do?")

# callback function for start button
def onStart(removeStartButton):
    # remove the start button
    removeStartButton()
    # create an empty dictionary to store groceries
    groceries = {}
    # create the button grid with add, remove, print, and cost functions
    CreateButtonGrid(
        lambda: additem(groceries), 
        lambda: remove(groceries), 
        lambda: printing(groceries),
        lambda: cost(groceries))
    # create the exit button
    CreateEndButton()
    # initial prompt
    prompt()  

if __name__ == "__main__":
    # create the main window 
    CreateRoot()
    # create the GUI elements
    GuiElements()
    # create the start button and pass the removeStart function as callback
    removeStart = CreateStartButton(lambda: onStart(removeStart))
    # start the main event loop
    Start()
