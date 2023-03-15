# create a function to build a recipe for the recipe class
def create_recipe(recipe):

    # Get a name for the recipe
    name_recipe = input('Name your recipe: ')

    # create a list of ingredients
    ingredients_recipe = []
    while True:
        x = input('Add ingredient, type "stop" to end: ')

        if x == 'stop':
            break
        else:
            ingredients_recipe.append(x)

    # create a dictionary with the steps to make the recipe
    process_recipe = {}
    n = 1
    while True:
        x = input(f'Add step {n}, type "stop" to end: ')

        if x == 'stop':
            break
        else:
            process_recipe[f'Step {n}'] = x
            n += 1

    return recipe(name_recipe, ingredients_recipe, process_recipe)

