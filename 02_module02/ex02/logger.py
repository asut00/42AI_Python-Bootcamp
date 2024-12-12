# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 11:32:04 by asuteau           #+#    #+#              #
#    Updated: 2024/06/12 11:32:09 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import time
from random import randint
import os
import getpass

#... your definition of log decorator...

def log(func):
	def wrapper(*args, **kwargs):

		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()
		exec_time = (end_time - start_time) * 1000

		username = getpass.getuser()


		with open('machine.log', 'a') as f:
			f.write(f"({username})Running: {func.__name__.title()}\t[ exec-time = {exec_time:.3f} ms ]\n")

		return result

	return wrapper

class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.01)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(1)
		self.water_level += water_level
		print("Blub blub blub...")



if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)