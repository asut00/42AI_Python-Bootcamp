# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:29:17 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 10:29:22 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys

argc = len(sys.argv)


def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str


for i in range(1, argc):
	swapped_str = sys.argv[i].swapcase()
	reversed_str = reverse(swapped_str)
	print(reversed_str)
