# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:04:14 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 11:04:16 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(s = None):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	if not s:
		s = input("What is the text to analyze?\n>> ")
	elif not isinstance(s, str):
		print("AssertionError: argument is not a string")
		return
	s_len = len(s)
	print("The text contains ", s_len, " character(s):")
	count = 0
	for i in range(0, s_len):
		if (s[i].isupper()):
			count += 1
	print("- ", count, " upper letter(s)")
	count = 0
	for i in range(0, s_len):
		if (s[i].islower()):
			count += 1
	print("- ", count, " lower letter(s)")
	count = 0
	for i in range(0, s_len):
		if (s[i] in string.punctuation):
			count += 1
	print("- ", count, " punctuation mark(s)")
	count = 0
	for i in range(0, s_len):
		if (s[i].isspace()):
			count += 1
	print("- ", count, "space(s)")


if __name__ == "__main__":
	if len(sys.argv) > 2:
		print("Too many arguments")
	elif len(sys.argv) > 1:
		text_analyzer(sys.argv[1])
	else:
		text_analyzer()
