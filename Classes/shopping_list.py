# this class takes a list of recipes and identifies which ingredients are necessary to make all the recipes
class ShoppingList:
    def __init__(self, recipes: list):
        self.recipes = recipes

    def createShoppingList(self):
        items = list(tuple(self.recipes))
        return items

