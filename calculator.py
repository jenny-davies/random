from tkinter import *

# set global variable
num = ''

# function to update expression
def press(number):
    global num

    num = num + str(number)

    equation.set(num)

# function to evaluate expression
def equalpress():
    try:
        global num
        
        total = str(eval(num))
        equation.set(total)

        num = ''

    except:
        equation.set(" error ")

# function to clear contents
def clear():
    global num
    num = ''
    equation.set('')

# driver
if __name__ == "__main__":
    # create GUI
    gui = Tk()

    # set background
    gui.configure(background = '#595954')

    # set title
    gui.title('Calculator')

    # set configuration
    gui.geometry('500x300')

    equation = StringVar()

    # create text entry box
    expression_field = Entry(gui, textvariable = equation)

    # create grid for placing widgets
    expression_field.grid(columnspan = 4,
                          ipadx = 70)
    
    # create buttons
    button1 = Button(
    gui,
    text = '1',
    font = ('Arial', 22),
    command = lambda: press(1),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button1.grid(row = 2, column = 0)

    button2 = Button(
    gui,
    text = '2',
    font = ('Arial', 22),
    command = lambda: press(2),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button2.grid(row = 2, column = 1)

    button3 = Button(
    gui,
    text = '3',
    font = ('Arial', 22),
    command = lambda: press(3),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button3.grid(row = 2, column = 2)

    button4 = Button(
    gui,
    text = '4',
    font = ('Arial', 22),
    command = lambda: press(4),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button4.grid(row = 3, column = 0)

    button5 = Button(
    gui,
    text = '5',
    font = ('Arial', 22),
    command = lambda: press(5),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button5.grid(row = 3, column = 1)

    button6 = Button(
    gui,
    text = '6',
    font = ('Arial', 22),
    command = lambda: press(6),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button6.grid(row = 3, column = 2)

    button7 = Button(
    gui,
    text = '7',
    font = ('Arial', 22),
    command = lambda: press(7),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button7.grid(row = 4, column = 0)

    button8 = Button(
    gui,
    text = '8',
    font = ('Arial', 22),
    command = lambda: press(8),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button8.grid(row = 4, column = 1)

    button9 = Button(
    gui,
    text = '9',
    font = ('Arial', 22),
    command = lambda: press(9),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button9.grid(row = 4, column = 2)

    button0 = Button(
    gui,
    text = '0',
    font = ('Arial', 22),
    command = lambda: press(0),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    button0.grid(row = 5, column = 0)

    add = Button(
    gui,
    text = ' + ',
    font = ('Arial', 22),
    command = lambda: press('+'),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    add.grid(row = 2, column = 3)

    subtract = Button(
    gui,
    text = ' - ',
    font = ('Arial', 22),
    command = lambda: press('-'),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    subtract.grid(row = 3, column = 3)

    multiply = Button(
    gui,
    text = ' x ',
    font = ('Arial', 22),
    command = lambda: press('*'),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    multiply.grid(row = 4, column = 3)

    divide = Button(
    gui,
    text = ' / ',
    font = ('Arial', 22),
    command = lambda: press('/'),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    divide.grid(row = 5, column = 3)

    equal = Button(
    gui,
    text = ' = ',
    font = ('Arial', 22),
    command = equalpress,
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    equal.grid(row = 5, column = 2)

    clear = Button(
    gui,
    text = ' C ',
    font = ('Arial', 22),
    command = clear,
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    clear.grid(row = 5, column = 1)

    decimal = Button(
    gui,
    text = ' . ',
    font = ('Arial', 22),
    command = lambda: press('.'),
    bg = '#2E2E2B',
    fg = 'white',
    height = 1,
    width = 7
    )
    
    decimal.grid(row = 6, column = 0)

    # start GUI
    gui.mainloop()