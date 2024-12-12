# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 09:24:35 by asuteau           #+#    #+#              #
#    Updated: 2024/06/11 09:24:36 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# recipe.py

class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		# Check the name
		if not isinstance(name, str) or not name:
			print("Error: 'name' must be a non-empty string")
			exit(1)
		self.name = name

		# Check the cooking_lvl
		if not isinstance(cooking_lvl, int) or not (1 <= cooking_lvl <= 5):
			print("Error: 'cooking_lvl' must be an integer between 1 and 5")
			exit(1)
		self.cooking_lvl = cooking_lvl

		# Check the cooking_time
		if not isinstance(cooking_time, int) or cooking_time < 0:
			print("Error: 'cooking_time' must be a non-negative integer")
			exit(1)
		self.cooking_time = cooking_time

		# Check the ingredients
		if not isinstance(ingredients, list) or not all(isinstance(ing, str) for ing in ingredients):
			print("Error: 'ingredients' must be a list of strings")
			exit(1)
		self.ingredients = ingredients

		# Check the description
		if not isinstance(description, str):
			print("Error: 'description' must be a string")
			exit(1)
		self.description = description

		# Check the recipe_type
		if recipe_type not in ["starter", "lunch", "dessert"]:
			print("Error: 'recipe_type' must be either 'starter', 'lunch', or 'dessert'")
			exit(1)
		self.recipe_type = recipe_type
    
	def __str__(self):
		return (f"Recipe for {self.name}:\n"
				f"Cooking level: {self.cooking_lvl}\n"
				f"Cooking time: {self.cooking_time} minutes\n"
				f"Ingredients: {', '.join(self.ingredients)}\n"
				f"Description: {self.description}\n"
				f"Type: {self.recipe_type}")

# Example of creating a Recipe object
if __name__ == "__main__":
    recipe = Recipe(
        "Pancakes",
        2,
        15,
        ["flour", "milk", "eggs", "sugar", "butter"],
        "A simple and quick pancake recipe.",
        "dessert"
    )
    print(recipe)

