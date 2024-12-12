# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 09:25:04 by asuteau           #+#    #+#              #
#    Updated: 2024/06/13 09:25:06 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


class NumPyCreator:

	def from_list(self, dtype=None):
		return np.array(lst,dtype=dtype)

	def from_tuple(self, tpl):
		return np.array(tpl)

	def from_iterable(self, itr):
		return np.array(iter)

	def from_shape(self, shape, value=0):
		return np.full(shape, value)
	
	def random(self, shape):
		return np.random.random(shape)
	
	def identity(self, n):
		return np.identity(n)



if __name__=="__main__":

	npcreator = NumPyCreator()

	nlist = [1, 2, 3, 4]
	shape = (3, 4)
	value = 7
	n = 4


	isitanarray = npcreator.identity(n)

	print(isitanarray)
	print(type(isitanarray))
