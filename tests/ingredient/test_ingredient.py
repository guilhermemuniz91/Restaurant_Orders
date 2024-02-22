from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Initialization of ingredients
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")
    ingredient3 = Ingredient("ovo")

    # testing functions
    assert ingredient1.name == "farinha"
    assert ingredient1.restrictions == {Restriction.GLUTEN}

    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    assert ingredient1.__hash__() == ingredient2.__hash__()
    assert ingredient1.__hash__() != ingredient3.__hash__()

    assert ingredient1.__repr__() == "Ingredient('farinha')"
    assert ingredient1.__repr__() == ingredient2.__repr__()
