# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 09:24:23 by asuteau           #+#    #+#              #
#    Updated: 2024/06/11 09:24:26 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe
import time

class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		if not isinstance(name, str) or not name:
			print("Error: Name must be a string")
			exit(1)
		self.name = name
		self.creation_date = datetime.now()
		self.last_update = creation_date
		self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
	
	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name {name} and returns the instance"""
		for type in self.recipes_list.values():
			for recipe in type:
				if recipe.name == name:
					print(recipe)
					return(recipe)

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type"""
		print(f"The {recipe_type}s are :")
		for recipe in self.recipes_list[recipe_type]:
			print(recipe)
	
	def add_recipe(self, recipe):
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = datetime.now()

	def __str__(self):
		recipes_str = "\n".join([f"  - {recipe}" for recipe in self.recipes_list])
		return (f"Book name : {self.name}:\n"
				f"Last update : {self.last_update}\n"
	 			f"Creation date: {self.creation_date} minutes\n"
	 			f"Recipes list:\n{recipes_str}\n")
	