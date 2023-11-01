################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ <
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at
# different temperatures to craft special materials.
#
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
# Crear una clase llamada Oven
class Oven:
    def __init__(self):
        self.ingredients = []
        self.temperature = 0

    def add(self, item):
        self.ingredients.append(item)

    def freeze(self):
        self.temperature = -100

    def boil(self):
        self.temperature = 100

    def wait(self):
        pass

class RecipeBook:
    def __init__(self):
        self.recipes = {
            (frozenset(["water", "air"]), -100): "snow",
            (frozenset(["lead", "mercury"]), 100): "gold",
            (frozenset(["cheese", "dough", "tomato"]), 100): "pizza",
            # Agrega aquí más recetas...
        }

    def get_output(self, ingredients, temperature):
        recipe_key = (frozenset(ingredients), temperature)
        if recipe_key in self.recipes:
            return self.recipes[recipe_key]
        else:
            raise ValueError("No se encontró ninguna receta que coincida con los ingredientes y la temperatura proporcionados.")

def make_oven():
    return Oven()

def make_recipe_book():
    return RecipeBook()

# Esta función usa el horno que le pasamos como parámetro
def alchemy_combine(oven, recipe_book, ingredients, temperature):

    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return recipe_book.get_output(oven.ingredients, oven.temperature)
