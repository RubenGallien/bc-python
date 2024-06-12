from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name, recipes_list, last_update=datetime.now(), creation_day=datetime.now()):
        expected_keys = {"starter", "lunch", "dessert"}
        if not name or not isinstance(name, str):
            print("Put a name for your book")
            exit(1)
        if not last_update or not isinstance(last_update, datetime):
            print("You need to put the date of the last update (YYYY-MM-DD HH-MM)")
            exit(1)
        if not creation_day or not isinstance(creation_day, datetime):
            print("You need to put the date of the creation (YYYY-MM-DD)")
            exit(1)
        if recipes_list:
            if set(recipes_list.keys()) != expected_keys:
                print("starter, lunch, dessert only allowed for the recipes list")
                exit(1)
        if not recipes_list or not isinstance(recipes_list, dict):
            print("Put a list of recipes")
            exit(1)
        self.name = name
        self.recipes_list = recipes_list
        self.last_update = last_update
        self.creation_day = creation_day

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for r in self.recipes_list.keys():
            if (self.recipes_list[r] == name):
                print(self.recipes_list[r])
                break;
        print("no recipe")