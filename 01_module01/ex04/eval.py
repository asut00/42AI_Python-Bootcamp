# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 12:52:09 by asuteau           #+#    #+#              #
#    Updated: 2024/06/11 12:52:10 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Evaluator:

	@staticmethod
	def zip_evaluate(coefs, words):
		w_len = len(words)
		c_len = len(coefs)
		if not (w_len == c_len):
			return -1
		zipped_data = zip(words, coefs)
		list_data = list(zipped_data)
		res = 0
		for elem in list_data:
			res += len(elem[0]) * elem[1]
		print(res)

	@staticmethod
	def enumerate_evaluate(coefs, words):
		w_len = len(words)
		c_len = len(coefs)
		if not (w_len == c_len):
			return -1
		i = 0
		res = 0
		for index in enumerate(words):
			res += len(index[1]) * coefs[index[0]]
		print(res)

if __name__ == "__main__":
	words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas"]
	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
	Evaluator.zip_evaluate(coefs, words)
	Evaluator.enumerate_evaluate(coefs, words)