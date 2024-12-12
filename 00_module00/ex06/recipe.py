# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 15:09:51 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 15:09:53 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# cookbook = dict()

cookbook = {}

cookbook["The Sandwich"] = {
	'ingredients': ["ham", "bread", "cheese", "tomatoes"],
	'meal': "lunch",
	'prep_time': 10,
}

cookbook["The Cake"] = {
	'ingredients': ["flowr", "sugar", "eggs"],
	'meal': "dessert",
	'prep_time': 60,
}

cookbook["The Salad"] = {
	'ingredients': ["avocado", "arugula", "tomatoes", "spinach"],
	'meal': "lunch",
	'prep_time': 15,
}

def print_recipe_names(dict):
	for i in dict:
		print(i)

def print_recipe_details(name):
	print("Name:", name)
	print("Ingredients:", end = " ")
	for i in cookbook[name]["ingredients"]:
		print(i, end = ", ")
	print("\nPrep time:", cookbook[name]["prep_time"], "min")

def delete_recipe(name):
	cookbook.pop(name)

def add_recipe():
	name = input("Enter a name:\n")
	ingredients = input("Enter ingredients (separated by commas):\n").split(',')
	meal_type = input("Enter a meal type:\n")
	prep_time = input("Enter a preparation time:\n")

	cookbook[name] = {
		'ingredients':[ingredient.strip() for ingredient in ingredients],
		'meal': meal_type,
		'prep_time': prep_time,
	}

print("Welcome to the Python Cookbook !")
print("List of available option :")
print("\t1: Add a recipe")
print("\t2: Delete a recipe")
print("\t3: Print a recipe")
print("\t4: Print the cookbook")
print("\t5: Quit\n")

while (1):
	option = input("Please select an option:\n")
	print('\n')

	if (option == '1'):
		add_recipe()
		exit
	elif (option == '2'):
		del_name = input("Enter name of the recipe to delete:\n")
		delete_recipe(del_name)
	elif (option == '3'):
		prt_name = input("Enter name of the recipe to print:\n")
		print('\n')
		print_recipe_details(prt_name)
		print('\n')
	elif (option == '4'):
		for i in cookbook:
			print_recipe_details(i)
			print('\n')
	elif (option == '5'):
		print("Cookbook closed, Goodbye !")
		exit()
	else:
		print("Sorry this option does not exist")
		print("List of available option :")
		print("\t1: Add a recipe")
		print("\t2: Delete a recipe")
		print("\t3: Print a recipe")
		print("\t4: Print the cookbook")
		print("\t5: Quit\n")




# print_recipe_names(cookbook)


# print_recipe_details("The Sandwich")



# print("Before delete :")
# print(cookbook)

# delete_recipe("The Salad")

# print("\nAfter delete :")
# print(cookbook)



#add_recipe()

#print(cookbook)

# for i in cookbook:
# 	print(i)
# 	print_recipe_details(i)
# 	print("\n")