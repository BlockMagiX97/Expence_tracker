import tkinter

total = 0

# Logic part
def updateTotal(totalLabel, total):
    # Updates total
    totalLabel.config(text=str(total)+"$")

def close(frame, price, totalLabel):
    # Closes tab

        # Updates total
    global total
    total -= price

    updateTotal(totalLabel, total)
    frame.destroy()

def add(root, name, price, totalLabel):
    # Adds expence

        # Updates total
    global total
    total += price

        # Makes expence
    newFrame = tkinter.Frame(root)
    newLabel = tkinter.Label(newFrame, text=name)
    newPrice = tkinter.Label(newFrame, text="Price: " + str(price) + "$")
    closeButton = tkinter.Button(newFrame, command= lambda: close(newFrame, price, totalLabel), text="REMOVE")

        # Adds expence to the screen
    newLabel.grid(column=0, row=0)
    newPrice.grid(column=0, row=1)
    closeButton.grid(column=1, row=1)
    newFrame.pack()
    updateTotal(totalLabel, total)


# Graphical part
root = tkinter.Tk()

frame = tkinter.Frame(root)

totalLabel = tkinter.Label(frame, text=str(total)+"$")
totalLabel.grid(column=1, row=0)

labelEntry = tkinter.Entry(frame, width=25)
labelEntry.grid(column=0, row=1)
labelEntry.insert(0, "Insert a label for an expence")


priceEntry = tkinter.Entry(frame, width=25)
priceEntry.grid(column=1, row=1)
priceEntry.insert(0, "Insert a price in dollars")

addButton = tkinter.Button(frame, command=lambda: add(root, labelEntry.get(), float(priceEntry.get()), totalLabel), text = "ADD")
addButton.grid(column=2, row=1)

frame.pack()

root.mainloop()