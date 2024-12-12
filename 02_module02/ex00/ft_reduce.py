# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 10:06:55 by asuteau           #+#    #+#              #
#    Updated: 2024/06/12 10:06:58 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functools import reduce

def ft_reduce(f_to_apply, iterable):

	if not hasattr(iterable, '__iter__'):
		raise TypeError(f"{type(iterable).__name__} object is not iterable")

	if (len(iterable)) < 1:
	 	raise TypeError("reduce() of empty sequence with no initial value")
	

	res = iterable[0]


	for i in range(1, len(iterable)):
		try:
			res = f_to_apply(res, iterable[i])
		except Exception as e:
			raise ValueError(f"Error applying function to item {item}: {e}")

	return res
	






def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
ft_res = ft_reduce(add, numbers)
print(ft_res)  # Output: 15
nat_res = reduce(add, numbers)
print(nat_res)