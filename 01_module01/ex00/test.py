# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 09:24:44 by asuteau           #+#    #+#              #
#    Updated: 2024/06/11 09:24:46 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe
import time

recipe_test = Recipe(
	name="Pancakes",
	cooking_lvl=2,
	cooking_time=15,
	ingredients=["flour", "milk", "eggs", "sugar", "butter"],
	description="A simple and quick pancake recipe.",
	recipe_type="dessert"
)

recipe_test2 = Recipe(
	name="Cookies",
	cooking_lvl=2,
	cooking_time=15,
	ingredients=["flour", "milk", "eggs", "sugar", "butter"],
	description="A simple and quick pancake recipe.",
	recipe_type="dessert"
)

print("***** Recipe print test *****")
print(recipe_test)
print()
    
book_test = Book(
	name = "Grandma's cookbook",
	last_update = time.time(),
	creation_date = time.time(),
	recipes_list = {
		'starter': {},
		'lunch' : {},
		'dessert' : {},
	},
)

print("***** Book init print test *****")
print(book_test)
print()

book_test.add_recipe(recipe_test)
book_test.add_recipe(recipe_test2)


print("***** get_recipes_by_types print test *****")
book_test.get_recipes_by_types("dessert")
print()

print("***** get_recipes_by_name print test *****")
book_test.get_recipe_by_name("Pancakes")
