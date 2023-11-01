from question3 import alchemy_combine, make_oven, make_recipe_book

def test_alchemy_combine():
  recipe_book = make_recipe_book()

  assert alchemy_combine(
    make_oven(),
    recipe_book,
    ["lead", "mercury"],
    5000
  ) == "gold"

  assert alchemy_combine(
    make_oven(),
    recipe_book,
    ["water", "air"],
    -100
  ) == "snow"

  assert alchemy_combine(
    make_oven(),
    recipe_book,
    ["cheese", "dough", "tomato"],
    150
  ) == "pizza"