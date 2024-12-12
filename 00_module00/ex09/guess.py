# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 17:55:49 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 17:55:51 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

def str_isdigit(s):
	for i in range(0, len(s)):
		if not (s[i].isdigit()):
			return 0
	return 1

secret_num = random.randint(1, 99)
attempts = 1

while (1):
	user_input = input("What's your guess between 1 and 99?\n>> ")
	if (user_input == "exit"):
		print("Goodbye")
		exit()
	elif (secret_num == 42 and int(user_input) == 42):
		print("The answer to the ultimate question of life, the universe and everything is 42.")
		print("Congratulations you've got it!")
		print("You figured it out in", attempts, "attempts")
		exit()
	elif(not str_isdigit(user_input)):
		print("That's not a number.")
	elif(int(user_input) > secret_num):
		print("Too high!")
	elif(int(user_input) < secret_num):
		print("Too low!")
	elif(int(user_input) == secret_num):
		print("Congratulations you've got it!")
		print("You figured it out in", attempts, "attempts")
		exit()
	attempts += 1