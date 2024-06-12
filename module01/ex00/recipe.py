class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description="None"):
        if not isinstance(name, str) or not name:
            print("The name of the recipe need to be a string")
            exit(1)
        if not isinstance(cooking_lvl, int) or not cooking_lvl:
            print("The cooking level needs to be a number")
            exit(1)
        elif cooking_lvl < 1 or cooking_lvl > 5:
            print("Cooking level is between 1 and 5")
            exit(1)
        if not isinstance(cooking_time, int) or not cooking_time:
            print("The cooking is a number, in minutes")
            exit(1)
        elif cooking_time < 0:
            print("The cookigng time is a POSITIVE number")
            exit(1)
        if not all(isinstance(s, str) for s in ingredients) or not ingredients:
            print("Ingredients needs to be a list of strings")
            exit(1)
        if isinstance(recipe_type, str) and recipe_type:
            if (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
                print("recipe_type is a starter or a lunch or a dessert")
        else:
            print("recipe is a string")
            exit(1)
        if not isinstance(description, str) or not description:
            print("Description needs to be a string")
            exit(1)
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the streing to print with the recipe info"""
        txt = ""
        txt += f"The recipe : {self.name} has a difficult of {self.cooking_lvl} (min 1 and max 5) and take {self.cooking_time} minutes to cook\n"
        txt += f"For this recipe, u will need : "
        for item in self.ingredients:
            txt += item + ", "
        txt += f"\nDescription : {self.description}\n"
        txt += f"The recipe is for {self.recipe_type}"
        return txt