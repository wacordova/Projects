# Importing everything from the tkinter module
from tkinter import *

# Initializing tkinter
root = Tk()

# Setting the width and height of the GUI application
root.geometry("430x500")

# Declaring an empty string variable
Expression = ""

# Defining the function that will set expressions and answers to the user
def SetExpression(num):
    global expression
    expression = expression + str(num)
    value.set(expression)

# Defining the function that will calculate the expression entered by the user
def Calculator():
    try:
        global expression
        Answer = str(eval(expression))
        value.set(answer)
    except:
        value.set("Enter an expression")
        expression = ""

# Defining a function to clear everything in the expression
def clear():
    global expression
    expression = ""
    value.set(expression)

# Declaring a variable for font (font type, size)
LargeFont = ('Verdana', 15)
SmallFont = ('Verdana', 10)

# Declaring a variable to take the value of the expression entered by the user
value = StringVar("Enter Expression")

# Entry widget to take expression from the user and to show the calaculations
Entry(root, textvariable=value, font = LargeFont).grid(row = 0, column = 0, columnspan = 4, ipadx = 70)

# Some basic buttons that will set values in the entry widget
Button(root, text="+", fg="red", command=lambda: SetExpression("+"), height=4, width=8).grid(row=1, column=0, pady=10)
Button(root, text="-", fg="red", command=lambda: SetExpression("-"), height=4, width=8).grid(row=2, column=0, pady=10)
Button(root, text="X", fg="red", command=lambda: SetExpression("*"), height=4, width=8).grid(row=3, column=0, pady=10)
Button(root, text="/", fg="red", command=lambda: SetExpression("/"), height=4, width=8).grid(row=4, column=0, pady=10)
Button(root, text="1", fg="red", command=lambda: SetExpression("1"), height=4, width=8).grid(row=1, column=1, pady=10)
Button(root, text="2", fg="red", command=lambda: SetExpression("2"), height=4, width=8).grid(row=1, column=2, pady=10)
Button(root, text="3", fg="red", command=lambda: SetExpression("3"), height=4, width=8).grid(row=1, column=3, pady=10)
Button(root, text="4", fg="red", command=lambda: SetExpression("4"), height=4, width=8).grid(row=2, column=1, pady=10)
Button(root, text="5", fg="red", command=lambda: SetExpression("5"), height=4, width=8).grid(row=2, column=2)
Button(root, text="6", fg="red", command=lambda: SetExpression("6"), height=4, width=8).grid(row=2, column=3, pady=10)
Button(root, text="7", fg="red", command=lambda: SetExpression("7"), height=4, width=8).grid(row=3, column=1, pady=10)
Button(root, text="8", fg="red", command=lambda: SetExpression("8"), height=4, width=8).grid(row=3, column=2, pady=10)
Button(root, text="9", fg="red", command=lambda: SetExpression("9"), height=4, width=8).grid(row=3, column=3, pady=10)
Button(root, text="0", fg="red", command=lambda: SetExpression("0"), height=4, width=8).grid(row=4, column=2, pady=10)
Button(root, text=".", fg="red", command=lambda: SetExpression("."), height=4, width=8).grid(row=4, column=1, pady=10)

# Adding the "=" button which will calculate and show the answer
Button(root, text="=", fg="red", command=Calculator, height=4, width=8).grid(row=4, column=3, pady=10)

# Adding the clear button which will call the clear() function
Button(root, text="Clear", fg="red", command=clear, height=4, width=20).grid(row=5, column=1, pady=10)

# Main loop to run the calculator again
root.mainloop()
