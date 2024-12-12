# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 12:24:48 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 12:24:49 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

argc = len(sys.argv)

def str_isdigit(s):
	for i in range(0, len(s)):
		if not (s[i].isdigit()):
			return 0
	return 1

if argc == 1:
	sys.exit()
elif not argc == 3:
	print("Error: wrong number of arguments")
elif not str_isdigit(sys.argv[1]) or not str_isdigit(sys.argv[2]):
	print("Error: arg is not int")
else:
	print("Sum:\t\t", int(sys.argv[1]) + int(sys.argv[2]))
	print("Difference:\t", int(sys.argv[1]) - int(sys.argv[2]))
	print("Product:\t", int(sys.argv[1]) * int(sys.argv[2]))
	if (int(sys.argv[2]) == 0):
		print("Quotient:\t ERROR (division by zero)")
		print("Remainder:\t ERROR (division by zero)")
	else:
		print("Quotient:\t", int(sys.argv[1]) / int(sys.argv[2]))
		print("Remainder:\t", int(sys.argv[1]) % int(sys.argv[2]))
