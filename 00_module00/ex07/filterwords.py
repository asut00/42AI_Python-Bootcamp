# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 17:26:09 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 17:26:11 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

argc = len(sys.argv)

def str_isdigit(s):
	for i in range(0, len(s)):
		if not (s[i].isdigit()):
			return 0
	return 1

if not argc == 3 or not isinstance(sys.argv[1], str) or not str_isdigit(sys.argv[2]):
	print("Error")
	exit()

input_str = sys.argv[1]

for char in string.punctuation:
	input_str = input_str.replace(char, ' ')

word_list = input_str.split()

final_list = [word for word in word_list if len(word) > int(sys.argv[2])]

print(final_list)
