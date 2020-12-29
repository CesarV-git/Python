from tkinter import *

window = Tk()
window.title("Simple Calculator")

text = Entry(window, font=("Calibri 22"))
text.grid(row=0, column=0, columnspan=5, pady=10, padx=20)
i = 0
# functions

def get_number(value):
    global i
    text.insert(i, value)
    i += 1

def clear_screen():
    text.configure(state="normal")
    text.delete(0, END)
    global i
    i = 0

def calculate():
    try:
        operation = text.get()
        result = eval(operation)
        text.delete(0, END)
        text.insert(0, result)
    except:
        text.delete(0, END)
        text.insert(0, "Error")
        global i
        i = 0
        text.configure(state="disabled")

def delete_last():
    state = text.get()
    new = state[:-1]
    text.delete(0,END)
    text.insert(0,new)


# Buttons - numbers
button1 = Button(window, text="1", width =5, height=2, command = lambda: get_number(1))
button2 = Button(window, text="2", width =5, height=2, command = lambda: get_number(2))
button3 = Button(window, text="3", width =5, height=2, command = lambda: get_number(3))
button4 = Button(window, text="4", width =5, height=2, command = lambda: get_number(4))
button5 = Button(window, text="5", width =5, height=2, command = lambda: get_number(5))
button6 = Button(window, text="6", width =5, height=2, command = lambda: get_number(6))
button7 = Button(window, text="7", width =5, height=2, command = lambda: get_number(7))
button8 = Button(window, text="8", width =5, height=2, command = lambda: get_number(8))
button9 = Button(window, text="9", width =5, height=2, command = lambda: get_number(9))
button0 = Button(window, text="0", width =5, height=2, command = lambda: get_number(0))

# Buttons - operators
button_AC = Button(window, text="AC", width =5, height=2, command = lambda :clear_screen())
button_point = Button(window, text=".", width =5, height=2, command = lambda: get_number("."))
button_par1 = Button(window, text="(", width =5, height=2, command = lambda: get_number("("))
button_par2 = Button(window, text=")", width =5, height=2, command = lambda: get_number(")"))
button_sum = Button(window, text="+", width =5, height=2, command = lambda: get_number("+"))
button_minus = Button(window, text="-", width =5, height=2, command = lambda: get_number("-"))
button_product = Button(window, text="x", width =5, height=2, command = lambda: get_number("*"))
button_division = Button(window, text="÷", width =5, height=2, command = lambda: get_number("/"))
button_result = Button(window, text="=", width =5, height=2, command = lambda: calculate())
button_retro = Button(window, text="del", width =5, height=2, command=lambda: delete_last())

# row 1
button7.grid(row= 1, column = 0 , padx= 5, pady= 5)
button8.grid(row= 1, column = 1, padx= 5, pady= 5)
button9.grid(row= 1, column = 2, padx= 5, pady= 5)
button_AC.grid(row= 1, column = 3, padx= 5, pady= 5)
button_retro.grid(row= 1, column = 4, padx= 5, pady= 5)

# row 2
button4.grid(row= 2, column = 0, padx= 5, pady= 5)
button5.grid(row= 2, column = 1, padx= 5, pady= 5)
button6.grid(row= 2, column = 2, padx= 5, pady= 5)
button_sum.grid(row= 2 , column = 3, padx= 5, pady= 5)
button_minus.grid(row= 2 , column = 4, padx= 5, pady= 5)

# row 3
button1.grid(row=3 , column = 0, padx= 5, pady= 5)
button2.grid(row= 3, column = 1, padx= 5, pady= 5)
button3.grid(row= 3, column = 2, padx= 5, pady= 5)
button_product.grid(row= 3, column = 3, padx= 5, pady= 5)
button_division.grid(row= 3, column = 4, padx= 5, pady= 5)

# row 4
button0.grid(row= 4, column = 0, padx= 5, pady= 5)
button_point.grid(row= 4, column = 1, padx= 5, pady= 5)
button_par1.grid(row= 4, column = 2, padx= 5, pady= 5)
button_par2.grid(row= 4, column = 3, padx= 5, pady= 5)
button_result.grid(row= 4, column =4 , padx= 5, pady= 5)

window.mainloop()