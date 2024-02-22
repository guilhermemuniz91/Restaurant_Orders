import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            header, *args = file_reader

            for dish, price, ingredient, recipe_amount in args:
                new_dish = Dish(dish, float(price))
                new_ingr = Ingredient(ingredient)

                if new_dish not in self.dishes:
                    new_dish.add_ingredient_dependency(
                        new_ingr, int(recipe_amount)
                    )
                    self.dishes.add(new_dish)
                else:
                    for elem in self.dishes:
                        if elem.name == dish:
                            elem.add_ingredient_dependency(
                                new_ingr, int(recipe_amount)
                            )
