import mealsdict

def get_ingredients():
    ingredient = input('Enter a list of ingredients separated by commas: ')
    ingredient_list = [item.strip() for item in ingredient.split(',')]
    print(f'You want to use: {ingredient_list}')

ingredients = get_ingredients()

