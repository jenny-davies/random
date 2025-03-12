from mealsdict import meals

def get_ingredients():
    ingredient = input('Enter a list of ingredients separated by commas: ')
    ingredient_list = [item.strip() for item in ingredient.split(',')]
    print(f'You want to use: {ingredient_list}')
    return ingredient_list

def search_meals_ingredients(user_ingredients):
    options_ingredients = []

    for meal, details in meals.items():
        meal_ingredients = details.get('ingredients', [])
        for ingredient in meal_ingredients:
            if ingredient in user_ingredients:
                options_ingredients.append(meal)
                break

    return options_ingredients

def get_required_difficulty():
    required_difficulty = input('Enter the difficulty level you need (easy, medium, hard): ')
    print(f'The required difficulty is: {required_difficulty}')
    return required_difficulty

def search_meals_difficulty(difficulty_selected, meal_options):
    options_difficulty = {}

    for meal in meal_options:
        difficulty = meals.get(meal, {}).get('difficulty', 'Unknown')
        if difficulty == difficulty_selected:
            options_difficulty[meal] = difficulty
        
    return options_difficulty

def get_required_speed():
    required_speed = input('Enter the speed you need (quick, medium, slow): ')
    print(f'The required speed is: {required_speed}')
    return required_speed

def search_meals_speed(speed_selected, meal_options):
    options_speed = {}

    for meal in meal_options:
        speed = meals.get(meal, {}).get('speed', 'Unknown')
        if speed == speed_selected:
            options_speed[meal] = speed

    return options_speed
