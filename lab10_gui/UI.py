from tkinter import *

# Create a root window
def CreateRoot():
    global root
    # main window 
    root = Tk()
    # window size
    root.geometry("800x800")
    # window title
    root.title("My Grocery List")
    # background color
    root.configure(background="#cbdbf5")
    # return the root window
    return root

def GuiElements():
    # create a title label
    title = Label(root, text="My Grocery List", font=('Times', 18), bg="#cbdbf5")
    # pack the title label with padding
    title.pack(padx=20, pady=20)

    # create a frame for the textbox
    textboxframe= Frame(root)
    # configure columns to take equal space
    textboxframe.columnconfigure(0, weight=1)
    textboxframe.columnconfigure(1, weight=1)

    global writeBox
    # create the textbox widget
    writeBox = Text(textboxframe, width=30, height=10, borderwidth=5,bg="#fff0d6", fg="#292525")
    # add the textbox to the frame and configure the layout
    writeBox.grid(row=1, column=0, sticky=W+E, columnspan=5, padx=20, pady=20)

    # pack the frame with fill 'x'
    textboxframe.pack(fill='x')

# function to create "MAKE A LIST" button
def CreateStartButton(onStart):
    startbtn = Button(root, text="MAKE A LIST", font='Courier', command=onStart, bg="#e3aeaa", fg="#292525")
    startbtn.pack(padx=10, pady=10)
    # return the destroy method of the button
    return startbtn.destroy


# function to create "Exit Program" button
def CreateEndButton():
    exitbutton = Button(root, text="Exit Program", font=('Courier', 18), command = root.destroy, bg="#e3aeaa", fg="#292525")
    exitbutton.pack(padx=10, pady=10)

# function to create grid of buttons
def CreateButtonGrid(additem, remove, printing, calculate):
    # helper function to create a button
    def CreateGridButton(text, comm, column):
        btn= Button(buttonframe, text=text, font=('Courier',18), command=comm, bg="#d1bcd6", fg="#292525")
        btn.grid(row=0, column=column, sticky=W+E)

    buttonframe = Frame(root)
    # configure columns to take equal space
    for i in range(4):
        buttonframe.columnconfigure(i, weight=1)

    # create buttons and add them to the grid
    CreateGridButton("Add Item", additem, 0)
    CreateGridButton("Remove Item", remove, 1)
    CreateGridButton("Print List", printing, 2)
    CreateGridButton("Calculate Cost", calculate, 3)
    # pack the frame
    buttonframe.pack(fill='x')

def createEntry(frame, labelName, row):
    # create label
    label = Label(frame, text=labelName, font=('Arial', 12), bg="#ebceb7", fg="#292525")
    label.grid(row=row, column=0, sticky=W+E, columnspan=1, padx=10, pady=10)

    # create entry box
    entryBox = Entry(frame, width=30, borderwidth=5, bg="#f5dfce", fg="#292525")
    entryBox.grid(row=row, column=1, sticky=W+E, columnspan=3, padx=10, pady=10)

    # return the get method of entry box
    return entryBox.get

def createEntries(labels, onConfirm):
    # create a global variable for entryframe
    global entryframe
    try:
        removeEntryFrame()
    except:
        pass
    # create entryframe as a frame
    entryframe = Frame(root)
    # create a list to hold all the entries
    values = []
    for i,label in enumerate(labels):
        entryframe.columnconfigure(i)
        # append the value of the entry to the values list
        values.append(createEntry(entryframe,label, i))
        # pack the entryframe
    entryframe.pack()
    global confirm
    # create a button with label Confirm, and font 'Arial' and sets command to onConfirm
    confirm = Button(root, text="Confirm", font='Arial', command=onConfirm, bg="#7e9e8e", fg="#ffffff")
    confirm.pack(padx=10, pady=10)
    # return the list of entries
    return values

def removeEntryFrame():
    #destroy the entryframe and confirm button
    entryframe.destroy()
    confirm.destroy()

def Start():
    # start the mainloop of the root
    root.mainloop()

def write(text):
    # write the text to the writeBox and then insert a new line
    writeBox.insert("end", text)
    writeBox.insert("end", "\n")