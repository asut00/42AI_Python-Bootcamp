# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:37:29 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 10:37:31 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys

argc = len(sys.argv)

if (sys.argv[1].isdigit() == 0):
	print("AssertionError: argument is not an integer")
elif (argc > 2):
	print("AssertionError: more than one argument are provided")
else:
	for i in range(1, argc):
		if (int(sys.argv[i]) == 0):
			print("I'm Zero.")
		elif (int(sys.argv[i]) % 2 == 0):
			print("I'm Even.")
		elif (int(sys.argv[i]) % 2 == 1):
			print("I'm Odd.")