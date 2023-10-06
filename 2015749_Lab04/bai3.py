from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def back():
    global expression
    expression = expression[:-1]
    equation.set(expression)

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light blue")
    gui.title("Simple Calculator")
    gui.geometry("270x150")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=75)

    bt0 = Button(gui, text='0', command=lambda: press(0), height=1, width=7)
    bt0.grid(row=6, column=0)
    bt1 = Button(gui, text='1', command=lambda: press(1), height=1, width=7)
    bt1.grid(row=5, column=0)
    bt2 = Button(gui, text='2', command=lambda: press(2), height=1, width=7)
    bt2.grid(row=5, column=1)
    bt3 = Button(gui, text='3', command=lambda: press(3), height=1, width=7)
    bt3.grid(row=5, column=2)
    bt4 = Button(gui, text='4', command=lambda: press(4), height=1, width=7)
    bt4.grid(row=4, column=0)
    bt5 = Button(gui, text='5', command=lambda: press(5), height=1, width=7)
    bt5.grid(row=4, column=1)
    bt6 = Button(gui, text='6', command=lambda: press(6), height=1, width=7)
    bt6.grid(row=4, column=2)
    bt7 = Button(gui, text='7', command=lambda: press(7), height=1, width=7)
    bt7.grid(row=3, column=0)
    bt8 = Button(gui, text='8', command=lambda: press(8), height=1, width=7)
    bt8.grid(row=3, column=1)
    bt9 = Button(gui, text='9', command=lambda: press(9), height=1, width=7)
    bt9.grid(row=3, column=2)

    cls = Button(gui, text='Cls', command = clear, height=1, width=7)
    cls.grid(row=2, column=0)
    back = Button(gui, text='Back', command = back, height=1, width=7)
    back.grid(row=2, column=1)
    blank = Button(gui, height=1, width=7)
    blank.grid(row=2, column=2)
    close = Button(gui, text='Close', command = gui.destroy, height=1, width=7)
    close.grid(row=2, column=3)
    decimal = Button(gui, text='.', command=lambda: press(
        '.'), height=1, width=7)
    decimal.grid(row=6, column=1)
    equal = Button(gui, text='=', command=equalpress, height=1, width=7)
    equal.grid(row=6, column=2)
    plus = Button(gui, text='+', command=lambda: press('+'), height=1, width=7)
    plus.grid(row=6, column=3)
    minus = Button(gui, text='-', command=lambda: press('-'),
                   height=1, width=7)
    minus.grid(row=5, column=3)
    mul = Button(gui, text='*', command=lambda: press('*'), height=1, width=7)
    mul.grid(row=4, column=3)
    div = Button(gui, text='/', command=lambda: press('/'), height=1, width=7)
    div.grid(row=3, column=3)
    
    gui.mainloop()
