from tkinter import *

# create GUI
window = Tk()
window.title('Weight converter')
window.geometry('500x500')

# create input variable
cups = IntVar()
item = StringVar()

# create functions for each conversion
def convert_cups_to_g():
    # get values
    cups1 = cups.get()
    item1 = item.get()

    # convert to grams
    if item1 == 'Water':
        grams = float(cups1) * 0.24 * 1000
        Label(window, text = f'{grams} grams', 
              font = ('Arial', 12)).pack()
    
    elif item1 == 'Flour':
        grams = float(cups1) * 0.125 * 1000
        Label(window, text = f'{grams} grams', 
              font = ('Arial', 12)).pack()
    
    elif item1 == 'Sugar':
        grams = float(cups1) * 0.2 * 1000
        Label(window, text = f'{grams} grams', 
              font = ('Arial', 12)).pack()
        
    elif item1 == 'Butter':
        grams = float(cups1) * 0.227 * 1000
        Label(window, text = f'{grams} grams', 
              font = ('Arial', 12)).pack()
        
    elif item1 == 'Milk':
        grams = float(cups1) * 0.245 * 1000
        Label(window, text = f'{grams} grams', 
              font = ('Arial', 12)).pack()

# create labels and entry fields
Label(window, text = 'Enter weight in cups: ', 
      font = ('Arial', 14)).pack()

Entry(window, textvariable = cups).pack()

Label(window, text = 'Enter item to convert: ',
      font = ('Arial', 14)).pack()

Entry(window, textvariable = item).pack()

# create buttons
Button(window, text = 'Convert to grams', 
       bg = 'grey', 
       command = convert_cups_to_g).pack()

# run
window.mainloop()