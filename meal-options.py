from mealsdict import meals

def get_ingredients():
    ingredient = input('Enter a list of ingredients separated by commas: ')
    ingredient_list = [item.strip() for item in ingredient.split(',')]
    print(f'You want to use: {ingredient_list}')

search_list = get_ingredients()

def search_meals(ingredients):
    options = []

    for meal, details in meals.items():
        ingredients = details.get('ingredients', [])
        for ingredient in search_list:
            if ingredient in ingredients:
                options.append(meal)
                break

    return options

all_meal_options = search_meals(search_list)

print(f'You could make: {all_meal_options}')