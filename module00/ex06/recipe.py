def p_recipe_name(recette):
   for x in recette.items():
      print(x[0])

def p_recipe_details(name):
    ing = "Ingredients = "
    meal = "Type of Meal = "
    prep = "Preparation times = "
    print(ing)
    print(f"{'-'* len(ing)}")
    for x in name["ingredients"]:
        print(x)
    print()
    print(meal)
    print(f"{'-'* len(meal)}")
    print(name["meal"])
    print()
    print(prep)
    print(f"{'-'* len(prep)}")
    print(f'{name["prep_time"]} minutes')

def del_recipe(cookbook, name):
    del(cookbook[name])

def add_recipe(cookbook):
    print("Enter a name :")
    name = input()
    print("Enter ingredients :")
    new_lst = []
    for _ in range(4):
        data = input()
        new_lst.append(data)
    print("Enter a meal type:")
    meal = input()
    print("Enter a preparation time :")
    prep = input()
    new_dict = {"ingredients" : new_lst, "meal" : meal, "prep_time" : int(prep)}
    cookbook[name] = new_dict

def print_option():
 print("List of available option :")
 print("\t1: Add a recipe")
 print("\t2: Delete a recipe")
 print("\t3: Print a recipe")
 print("\t4: Print the cookbook")
 print("\t5: Quit")
 print()

cookbook = {
	"Sandwich" : {
		"ingredients" :["ham", "bread", "cheese","tomatoes"],
		"meal" : "lunch",
		"prep_time": 10
	},
	"Cake" : {
		"ingredients" :["flour", "sugar", "eggs"],
		"meal": "dessert",
		"prep_time" : 60
	},
	"Salad" : {
		"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
		"meal" : "lunch",
		"prep_time" : 15
	}
}
print_option()
while (1):
    print("Please select an option : ")
    choice = input()
    print()
    if choice == "1":
        add_recipe()
    if choice == "2":
        print("What recipe do you want delete ?")
        delete = input()
        del_recipe(cookbook(delete))
    if choice == "3":
        print("Please enter a recipe name to get its details")
        name = input()
        p_recipe_details(name)
    if choice == "4":
        p_recipe_name(cookbook)
    elif choice == "5":
        print("Goodbye !")
        exit()
    else:
        print("Sorry, this option doesnt exist")
        print_option()
