# the class creates a recipe buy taking in a name, a list of ingredients,
# and a dictionary consisting of the steps required to make it
class Recipe:
    def __init__(self, name: str, ingredients: list, process: dict):
        self.name = name
        self.ingredients = ingredients
        self.process = process

