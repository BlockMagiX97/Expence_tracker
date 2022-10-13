import tkinter

total = 0

def close(frame, price):
    total -= price
    
    frame.destroy()

def add(root, name, price):
    total += price

    newFrame = tkinter.Frame(root)
    newLabel = tkinter.Label(newFrame, text=name)
    newPrice = tkinter.Label(newFrame, text=str(price) + "$")
    closeButton = tkinter.Button(newFrame, command= lambda: close(newFrame, price))

    newLabel.grid(column=0)
    newPrice.grid(column=1)
    closeButton.grid(column=2)
    
root = tkinter.Tk()



root.mainloop()