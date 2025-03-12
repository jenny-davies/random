from meals_options import *
from tkinter import *

# create GUI
window = Tk()
window.title('Meal planner')
window.geometry('800x500')

# create input variable
ingredients = StringVar()
difficulty = StringVar()
speed = StringVar()

# function to run search
def main():
    # get values
    ingredients1 = ingredients.get()
    difficulty1 = difficulty.get()
    speed1 = speed.get()

    ingredients1_list = [ingredients1.strip() for i in ingredients1.split(',')]

    # search for ingredients
    all_meals_ingredients = search_meals_ingredients(user_ingredients = ingredients1_list)

    if len(all_meals_ingredients) == 0:
        # return output for no matches
        Label(window, text = 'No meals match ingredients provided', 
              font = ('Arial', 12)).pack()
    
    elif len(all_meals_ingredients) > 0:
        # filter by difficulty
        all_meals_difficulty = search_meals_difficulty(difficulty_selected = difficulty1, 
                                                       meal_options = all_meals_ingredients)
        
        if len(all_meals_difficulty) == 0:
            # return output for no matches
            Label(window, text = 'No meals match ingredients and difficulty provided', 
                  font = ('Arial', 12)).pack()
            
        elif len(all_meals_difficulty) > 0:
            # filter by speed
            all_meals_speed = search_meals_speed(speed_selected = speed1,
                                                 meal_options = all_meals_difficulty)
            
            if len(all_meals_speed) == 0:
                # return output for no matches
                Label(window, text = 'No meals match ingredients, difficulty and speed selected',
                      font = ('Arial', 12)).pack()
                
            else:
                # else print output
                Label(window, text = f'You could make: {all_meals_speed}',
                      font = ('Arial', 12)).pack()

# create labels and entry fields
Label(window, text = 'Enter list of ingredients separated by commas: ', 
      font = ('Arial', 14)).pack()

Entry(window, textvariable = ingredients).pack()

Label(window, text = 'Enter difficulty level: ',
      font = ('Arial', 14)).pack()

Entry(window, textvariable = difficulty).pack()

Label(window, text = 'Enter required speed: ',
      font = ('Arial', 14)).pack()

Entry(window, textvariable = speed).pack()

# create button
Button(window, text = 'Suggest recipes', 
       bg = 'grey', 
       command = main).pack()

# run
window.mainloop()