# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 12:14:04 by asuteau           #+#    #+#              #
#    Updated: 2024/06/11 12:14:05 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random


def generator(text, sep=" ", option=None):
	
	if (not isinstance(text, str)):
		print("ERROR")
		exit(1)

	splitted_text = text.split(sep)

	if (option == None):
		for substring in splitted_text:
			yield substring
	elif (option == "shuffle"):
		random.shuffle(splitted_text)
		for substring in splitted_text:
			yield substring
	elif (option == "unique"):
		unique_list = list(set(splitted_text))
		for substring in unique_list:
			yield substring
	elif (option == "ordered"):
		splitted_text.sort()
		for substring in splitted_text:
			yield substring
	else:
		print("ERROR")


if __name__== "__main__":
	text = "hello.there"
	for substring in generator(text, sep="."):
		print(substring)
