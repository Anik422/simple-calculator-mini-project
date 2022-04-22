import math
from tkinter import *
from turtle import goto


def button_click(number):
    currenClick = myentry.get()
    myentry.delete(0, END)
    myentry.insert(0, str(currenClick) + str(number))


def button_clear():
    myentry.delete(0, END)


def button_addition():
    first_num = myentry.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    myentry.delete(0, END)


def button_subtraction():
    first_num = myentry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    myentry.delete(0, END)


def button_mulplication():
    first_num = myentry.get()
    global f_num
    global math
    math = 'mulplication'
    f_num = int(first_num)
    myentry.delete(0, END)


def button_division():
    first_num = myentry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    myentry.delete(0, END)


def buttonEqual():
    sce_num = myentry.get()
    myentry.delete(0, END)
    if math == 'addition':
        myentry.insert(0, f_num + int(sce_num))
    elif math == 'subtraction':
        myentry.insert(0, f_num - int(sce_num))
    elif math == 'mulplication':
        myentry.insert(0, f_num * int(sce_num))
    elif math == 'division':
        myentry.insert(0, f_num / int(sce_num))


root = Tk()
root.title("Calculator")

myentry = Entry(root, width=15, borderwidth=5,
                font=('default', 30), justify='right')
myentry.grid(row=0, column=0, columnspan=4, padx=10, pady=5)
myentry.focus_set()


# row 1 start
button_1 = Button(root, text='1', padx=30, pady=10,
                  command=lambda: button_click(1)).grid(row=1, column=0)

button_2 = Button(root, text='2', padx=30, pady=10,
                  command=lambda: button_click(2)).grid(row=1, column=1)

button_3 = Button(root, text='3', padx=30, pady=10,
                  command=lambda: button_click(3)).grid(row=1, column=2)

button_sub = Button(root, text='-', padx=30, pady=10,
                    command=button_subtraction).grid(row=1, column=3)

# row 1 end


# row 2 start
button_4 = Button(root, text='4', padx=30, pady=10,
                  command=lambda: button_click(4)).grid(row=2, column=0)

button_5 = Button(root, text='5', padx=30, pady=10,
                  command=lambda: button_click(5)).grid(row=2, column=1)

button_6 = Button(root, text='6', padx=30, pady=10,
                  command=lambda: button_click(6)).grid(row=2, column=2)

button_div = Button(root, text='/', padx=30, pady=10,
                    command=button_division).grid(row=2, column=3)
# row 2 end


# row 3 start
button_7 = Button(root, text='7', padx=30, pady=10,
                  command=lambda: button_click(7)).grid(row=3, column=0)

button_8 = Button(root, text='8', padx=30, pady=10,
                  command=lambda: button_click(8)).grid(row=3, column=1)

button_9 = Button(root, text='9', padx=30, pady=10,
                  command=lambda: button_click(9)).grid(row=3, column=2)

button_mul = Button(root, text='*', padx=30, pady=10,
                    command=button_mulplication).grid(row=3, column=3)
# row 3 end


# row 4 start
button_c = Button(root, text='C', padx=30, pady=10,
                  command=button_clear).grid(row=4, column=0)


button_0 = Button(root, text='0', padx=30, pady=10,
                  command=lambda: button_click(0)).grid(row=4, column=1)

button_equal = Button(root, text='=', padx=30, pady=10,
                      command=buttonEqual).grid(row=4, column=2)

button_add = Button(root, text='+', padx=30, pady=10,
                    command=button_addition).grid(row=4, column=3)

# row 4 end

root.mainloop()
