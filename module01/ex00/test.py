from recipe import Recipe
from book import Book
from datetime import datetime

# bolo = Recipe("Pates bolognaise", 2, 30, ["pates", "viande hachees"], "lunch", "cuire les pates, mettre de la viande")
# to_print = str(bolo)
# print(to_print)

expected_keys = {
	"starter":"entree",
	"lunch":"bol",
	"dessert" : "dessert"
}

mom_recipes = Book("maman", expected_keys)
mom_recipes.get_recipe_by_name("bolo")